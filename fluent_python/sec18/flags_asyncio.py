import asyncio

import aiohttp

from flags import BASE_URL, save_flag, show, main

async def get_flag(session, cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    # resp = await aiohttp.request('GET', url)
    async with session.get(url) as resp:
        image = await resp.read()
    return image

async def download_one(cc):
    async with aiohttp.ClientSession() as session:
        image = await get_flag(session, cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc

def download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in sorted(cc_list)]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()

    return len(res)

if __name__ == '__main__':
    main(download_many)
