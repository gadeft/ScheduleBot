import os

import httpx
from dotenv import load_dotenv

from src.api.v1.urls import urls
from src.api.v1.urls import Url


load_dotenv()
API_KEY = os.environ.get("API_KEY")
headers = {"X-Api-Key": API_KEY}


async def lookup(url) -> dict:
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, headers=headers, timeout=None)

    return resp.json()


async def get_schedule(day_id = None, week_id = None, group_id = None, lecturer_id = None) -> dict:
    params = dict()

    if day_id is not None:
        params['day_id'] = day_id
    if week_id is not None:
        params['week_id'] = week_id
    if group_id is not None:
        params["group_id"] = group_id
    if lecturer_id is not None:
        params["lecturer_id"] = lecturer_id

    async with httpx.AsyncClient() as client:
        resp = await client.get(urls[Url.SCHEDULE], params=params, headers=headers, timeout=None)

    return resp.json()

