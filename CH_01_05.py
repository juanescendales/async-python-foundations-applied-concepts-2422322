import asyncio
from datetime import datetime
import click


async def sleep_five(space = ""):
    print(space+"Sleep five start")
    await asyncio.sleep(5)
    print(space+"Sleep five finish")


async def sleep_three_then_five():
    print("Sleep tree then five start")
    print("- Sleep tree start")
    await asyncio.sleep(3)
    print("- Sleep tree finish")
    await sleep_five("- ")
    print("Sleep tree then five finish")


async def main():
    await asyncio.gather(sleep_five(),sleep_three_then_five())


start = datetime.now()
asyncio.run(main())
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")
