import typing
from Orbit import Orbit
from numpy import array
from math import sin, cos, pi
from Models.Planet import Planet


class Station:
    planet = Planet(6.4e6, 6e24)
    name = "James Webb Telescope"
    heightVector: array = array([408e3 + planet.radius, 0])
    velocity: float = 7.66e3
    throttle: float = 0
    maxThrottle = 4
    headingVector: array = array([velocity, 90])
    throttleVector: array = array([throttle * maxThrottle, 90])
    orbit: Orbit
    last_update: float = 0
    speed = 10

    def __init__(self):
        self.orbit = Orbit()

    def getPosition(self):
        return (self.heightVector[0] * cos(self.heightVector[1]),
                self.heightVector[0] * sin(self.heightVector[1]))

    def getAngularVelocity(self):
        return self.headingVector[0] / self.heightVector[0]

    def updateAngle(self, deltaTime):
        deltaAngle = self.getAngularVelocity() * deltaTime
        self.headingVector[1] += deltaAngle
        self.heightVector[1] += deltaAngle
