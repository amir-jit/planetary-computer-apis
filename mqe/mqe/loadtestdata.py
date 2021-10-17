import asyncio
from pathlib import Path

import orjson
from pypgstac.load import DB, load_iterator, loadopt, tables


async def load_test_data() -> None:
    async with DB() as conn:
        with open("/opt/testdata/collection.json", "rb") as f:
            c = orjson.loads(f.read())
            await load_iterator([c], tables.collections, conn, loadopt.upsert)
        pathlist = Path("/opt/testdata/items/").glob("*.json")
        for path in pathlist:
            with open(str(path), "rb") as f:
                i = orjson.loads(f.read())
                await load_iterator([i], tables.items, conn, loadopt.upsert)


asyncio.run(load_test_data())
