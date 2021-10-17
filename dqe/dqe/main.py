#!/usr/bin/env python3
import logging
import os
from typing import Awaitable, Callable, Dict, List

from cogeo_mosaic.errors import NoAssetFoundError
from fastapi import FastAPI, Request, Response
from fastapi.openapi.utils import get_openapi
from morecantile.defaults import tms as defaultTileMatrices
from morecantile.models import TileMatrixSet
from starlette import status
from starlette.middleware.cors import CORSMiddleware
from titiler.application.middleware import (
    CacheControlMiddleware,
    LoggerMiddleware,
    TotalTimeMiddleware,
)
from titiler.core.errors import DEFAULT_STATUS_CODES, add_exception_handlers

from dqe.config import get_settings
from dqe.db import close_db_connection, connect_to_db
from dqe.endpoints import collection, item, pg_mosaic, vrt
from dqe.middleware import count_data_requests, trace_request
from pqecommon.logging import init_logging
from pqecommon.openapi import fixup_schema

# Initialize logging
init_logging("dqe")
logger = logging.getLogger(__name__)

# Get the root path if set in the environment
APP_ROOT_PATH = os.environ.get("APP_ROOT_PATH", "")

settings = get_settings()

app = FastAPI(
    title=settings.title,
    openapi_url=settings.openapi_url,
    root_path=APP_ROOT_PATH,
)

app.include_router(
    item.pc_tile_factory.router,
    prefix=get_settings().item_endpoint_prefix,
    tags=["Item tile endpoints"],
)

app.include_router(
    collection.collection_mosaic_factory.router,
    prefix=get_settings().collection_endpoint_prefix,
    tags=["Collection tile endpoints"],
)

app.include_router(
    pg_mosaic.pgstac_mosaic_factory.router,
    prefix=get_settings().mosaic_endpoint_prefix,
    tags=["PgSTAC Mosaic endpoints"],
)

if settings.feature_flags.VRT:
    app.include_router(
        vrt.vrt_factory.router, prefix="/vrt", tags=["Planetary Computer VRT Service"]
    )


@app.middleware("http")
async def _count_data_requests(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    return await count_data_requests(request, call_next)


@app.middleware("http")
async def _trace_requests(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    return await trace_request(request, call_next)


add_exception_handlers(
    app, {**DEFAULT_STATUS_CODES, NoAssetFoundError: status.HTTP_404_NOT_FOUND}
)  # type: ignore

app.add_middleware(CacheControlMiddleware, cachecontrol="public, max-age=3600")
app.add_middleware(TotalTimeMiddleware)

if get_settings().debug:
    app.add_middleware(LoggerMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event() -> None:
    """Connect to database on startup."""
    await connect_to_db(app)


@app.on_event("shutdown")
async def shutdown_event() -> None:
    """Close database connection."""
    await close_db_connection(app)


@app.get("/")
async def read_root() -> Dict[str, str]:
    return {"Hello": "Planetary Developer!"}


@app.get("/tileMatrixSets")
async def matrix_list() -> List[str]:
    return defaultTileMatrices.list()


@app.get("/tileMatrixSets/{tileMatrixSetId}")
async def matrix_definition(tileMatrixSetId: str) -> TileMatrixSet:
    logger.info(
        "Matrix definition requested",
        extra={
            "custom_dimensions": {
                "tileMatrixSetId": tileMatrixSetId,
            }
        },
    )
    return defaultTileMatrices.get(tileMatrixSetId)


def custom_openapi() -> Dict:
    if not app.openapi_schema:
        schema = get_openapi(
            title="Preview of Tile Access Features",
            version=get_settings().api_version,
            routes=app.routes,
        )
        app.openapi_schema = fixup_schema(app.root_path, schema)
    return app.openapi_schema


app.openapi = custom_openapi  # type: ignore
