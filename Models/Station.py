import typing
from Orbit import Orbit
from numpy import array


class Station:
    name = "James Webb Telescope"
    height: array = array([1.5e9, 0])
    heading: tuple[float, float] = (1, 0)
    throttleVector: tuple[float, float] = (1, 0)
    orbit: Orbit

    def __init__(self):
        self.orbit = Orbit()

