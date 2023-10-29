import asyncio
import Models.Station
from numpy import array
from numpy.linalg import norm as vect_len
from time import time


s = Models.Station.StationV2()
delta = 1
warp = 100


async def main():
    time_ = time()
    while True:
        s.update()
        await asyncio.sleep(delta)


loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()