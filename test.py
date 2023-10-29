from Models.Station import Station
from time import time, sleep
from numpy import array
from matplotlib import pyplot as plt, patches
import asyncio


start = time()
s = Station("Earth")
s.timer.setTimeScale(100)
arr_x, arr_y = [], []


async def runStation():
    for _ in range(100):
        await asyncio.sleep(1)
        print(s.timer.time())
        x, y = s.getCoordinates()
        arr_x.append(x)
        arr_y.append(y)
    loop.stop()
    plt.figure()
    plt.plot(arr_x, arr_y)
    plt.xlabel('X (km)')
    plt.ylabel('Y (km)')
    plt.title('Orbit Plot')
    plt.axis('equal')  # Ensure the aspect ratio is equal
    plt.grid(True)
    plt.show()


loop = asyncio.get_event_loop()
loop.create_task(s.timer.runTime())
loop.create_task(runStation())
loop.run_forever()
