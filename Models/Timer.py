from asyncio import sleep
from time import time


class Timer:
    def __init__(self, scale: int = 1):
        self.local_time = time()
        self.timeScale = scale
        self.__delta = 1

    def setTimeScale(self, scale):
        self.timeScale = scale

    async def runTime(self):
        while True:
            await sleep(self.__delta)
            self.local_time += self.timeScale * self.__delta

    def time(self):
        return self.local_time

