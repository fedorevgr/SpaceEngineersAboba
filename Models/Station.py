import typing
from Orbit import Orbit


class Station:
    Name = "James Webb Telescope"
    Height: float = 1.5e9
    Heading: tuple[float, float, float] = (0, 0, 0)
    ThrottleVector: tuple[float, float, float] = (0, 0, 0)
    orbit: Orbit

    def __init__(self):
        self.orbit = Orbit()

