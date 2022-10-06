import asyncio
import aiohttp
import time


async def load_yandex():
    with aiohttp.ClientSession() as s:
        resp = await s.get('https://ya.ru')
        print(await resp.json())


async def load_google():
    with aiohttp.ClientSession() as s:
        resp = await s.get('https://google.com')
        print(await resp.json())


async def main():
    while True:
        await load_yandex()
        await load_google()

        time.sleep(1)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
