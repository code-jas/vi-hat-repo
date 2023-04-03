import requests
import asyncio
import aiohttp



def left():
    get = requests.get("http://192.168.4.4/left/active")


def right():
    get = requests.get("http://192.168.4.1/right/active")


async def make_request(url, delay):
    await asyncio.sleep(delay)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main_req():
    req1 = "http://192.168.4.1/right/active"
    req2 = "http://192.168.4.4/left/active"
    tasks = [
        asyncio.create_task(make_request(req1, 0.2)),
        asyncio.create_task(make_request(req2, 0))
    ]
    result = await asyncio.gather(*tasks)
    print(result)

while(True):

    state = input('input state: \n')

    if state == 'r':
        get = requests.get("http://192.168.4.1/right/active")

    if state == 'l':
        get = requests.get("http://192.168.4.4/left/active")

    if state == 'rl':
        asyncio.run(main_req())

    if state == 'q':
        break

    print('\n')
