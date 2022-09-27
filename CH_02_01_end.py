from datetime import datetime
from pprint import pprint
import asyncio

import aiohttp
import click

urls = [
    "https://4udy5hmswf.execute-api.us-east-1.amazonaws.com/Prod/clock?timezone=",
    "https://4udy5hmswf.execute-api.us-east-1.amazonaws.com/Prod/clock?timezone=",
    "https://4udy5hmswf.execute-api.us-east-1.amazonaws.com/Prod/clock?timezone=",
    "https://4udy5hmswf.execute-api.us-east-1.amazonaws.com/Prod/clock?timezone=",
    "https://4udy5hmswf.execute-api.us-east-1.amazonaws.com/Prod/clock?timezone=",
]


async def fetch_args(session, url):
    async with session.get(url) as response:
        data = await response.json()
        return data["message"]


async def main():
    async with aiohttp.ClientSession() as session:
        # create a collection of coroutines(can be done with comprehension )
        fetch_coroutines = []
        for url in urls:
            fetch_coroutines.append(fetch_args(session, url))
        # waik up coroutines with gather
        data = await asyncio.gather(*fetch_coroutines)
        pprint(data)


start = datetime.now()
asyncio.run(main())
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")
