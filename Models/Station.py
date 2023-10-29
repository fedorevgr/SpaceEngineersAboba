from Models.Orbit import Orbit
from numpy import array, linspace, linalg
from poliastro.bodies import *
from astropy import units as u

from Models.Timer import Timer


BODIES = {
    "Earth": Earth,
    "Mercury": Mercury,
    "Moon": Moon,
    "Sun": Sun,
    "Mars": Mars
}


class Station:
    def __init__(self, bodyName: str = "Earth", height: float = 403e3, velocity: float = 7.33e3):

        self.planet = BODIES[bodyName]

        self.coordinates = array(
            [
                height + self.planet.R.value,
                0,
                0
            ]
        ) * u.m

        self.velocity = array(
            [
                0,
                velocity,
                0
            ]
        ) * u.m / u.s

        self.timer = Timer()

        self.lastChangeOfOrbit = self.timer.time() * u.s
        self.orbit = Orbit.from_vectors(
            attractor=self.planet,
            r=self.coordinates,
            v=self.velocity
        )

    def getOrbitCoordinates(self, points=100) -> list[float]:
        """
        Возвращает координаты точек принадлежащих орбите
        :param points:
        :return: ((x1, y1), (x2, y2), (x3, y3), ...)
        """
        times = linspace(0, self.orbit.period.to(u.s), points)

        positions = [tuple(self.orbit.propagate(time << u.s).r.value)[:2] for time in times]

        return positions

    def getCoordinates(self):
        return tuple(self.orbit.propagate(self.timer.time() * u.s).r.value)[:2]

    def blow(self, thrustVector: list, delta_time: float):
        """

        :param thrustVector:
        :param delta_time:
        :return:
        """
        thrustVector = array(thrustVector + [0])

        delta_time, timeElapsed = delta_time * u.s, (self.timer.time() * u.s - self.lastChangeOfOrbit)

        deltaInTime = 10 * u.s

        self.coordinates = self.orbit.propagate(timeElapsed).r
        nextCoordinates = self.orbit.propagate(timeElapsed + delta_time).r

        self.velocity = (nextCoordinates - self.coordinates) / deltaInTime

        thrustVector = thrustVector * u.m / (u.s * u.s)

        gValue = self.planet.k / (linalg.norm(self.coordinates) ** 2)
        rValue = linalg.norm(self.coordinates)

        gOneVector = ((self.coordinates.copy() * -1) / rValue) * gValue

        commonAcceleration = thrustVector + gOneVector

        deltaV = commonAcceleration * delta_time
        self.updateVelocity(deltaV)
        self.lastChangeOfOrbit = self.timer.time() * u.s

    def updateVelocity(self, delta):
        self.velocity += delta

        self.orbit = Orbit.from_vectors(
            attractor=self.planet,
            r=self.coordinates,
            v=self.velocity
        )
