import logging
from typing import Any, Callable, Coroutine, Dict, Optional

import attr
from pydantic import Field
from stac_fastapi.api.models import BaseSearchGetRequest, ItemCollectionUri
from stac_fastapi.pgstac.types.base_item_cache import BaseItemCache
from stac_fastapi.pgstac.types.search import PgstacSearch
from starlette.requests import Request
from typing_extensions import Annotated

from pccommon.redis import cached_result
from pcstac.contants import CACHE_KEY_BASE_ITEM

DEFAULT_LIMIT = 250

logger = logging.getLogger(__name__)


class PCSearch(PgstacSearch):
    # Increase the default limit for performance
    # Ignore "Illegal type annotation: call expression not allowed"
    limit: Annotated[Optional[int], Field(strict=True, ge=1, le=1000)] = DEFAULT_LIMIT


class RedisBaseItemCache(BaseItemCache):
    """
    Return the base item for the collection and cache by collection id.
    First check if the instance has a local cache of the base item, then
    try redis, and finally fetch from the database.
    """

    def __init__(
        self,
        fetch_base_item: Callable[[str], Coroutine[Any, Any, Dict[str, Any]]],
        request: Request,
    ):
        self._base_items: dict = {}
        super().__init__(fetch_base_item, request)

    async def get(self, collection_id: str) -> Dict[str, Any]:
        async def _fetch() -> Dict[str, Any]:
            return await self._fetch_base_item(collection_id)

        if collection_id not in self._base_items:
            cache_key = f"{CACHE_KEY_BASE_ITEM}:{collection_id}"
            self._base_items[collection_id] = await cached_result(
                _fetch, cache_key, self._request
            )

        return self._base_items[collection_id]


@attr.s
class PCItemCollectionUri(ItemCollectionUri):
    limit: Optional[int] = attr.ib(default=DEFAULT_LIMIT)  # type:ignore


@attr.s
class PCSearchGetRequest(BaseSearchGetRequest):
    limit: Optional[int] = attr.ib(default=DEFAULT_LIMIT)  # type:ignore
