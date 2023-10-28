import typing
from Orbit import Orbit
from numpy import array
from math import sin, cos
from Models.Planet import Planet


class Station:
    planet = Planet(6.4e6, 6e24)
    name = "James Webb Telescope"
    heightVector: array = array([408e3 + planet.radius, 0])
    headingVector: array = array([1, 90])
    throttleVector: array = array([1, 90])
    velocity = 7.66e3
    orbit: Orbit

    def __init__(self):
        self.orbit = Orbit()

    def getPosition(self):
        return (self.heightVector[0] * cos(self.heightVector[1]),
                self.heightVector[0] * sin(self.heightVector[1]))





s = Station()
print(s.getPosition())