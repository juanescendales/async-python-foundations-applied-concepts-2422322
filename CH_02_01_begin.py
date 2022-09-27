from datetime import datetime
from pprint import pprint

import click
import requests

urls = [
    "https://4udy5hmswf.execute-api.us-east-1.amazonaws.com/Prod/clock?timezone=",
    "https://4udy5hmswf.execute-api.us-east-1.amazonaws.com/Prod/clock?timezone=",
    "https://4udy5hmswf.execute-api.us-east-1.amazonaws.com/Prod/clock?timezone=",
    "https://4udy5hmswf.execute-api.us-east-1.amazonaws.com/Prod/clock?timezone=",
    "https://4udy5hmswf.execute-api.us-east-1.amazonaws.com/Prod/clock?timezone=",
]


def get_args(url):
    return requests.get(url).json()["message"]


start = datetime.now()
pprint([get_args(url) for url in urls])
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")
