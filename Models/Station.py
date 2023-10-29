from Models.Orbit import Orbit
from numpy import array, linspace, linalg
from poliastro.bodies import *
from astropy import units as u
from time import time


BODIES = {
    "Earth": Earth,
    "Mercury": Mercury,
    "Moon": Moon,
    "Sun": Sun,
    "Mars": Mars
}


class Station:

    def __init__(self,
                 bodyName: str,
                 height: float = 403e3,
                 velocity: float = 7.33e3,
                 timeScale: int = 1):

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

        self.lastChangeOfOrbit = time() * u.s

        self.orbit = Orbit.from_vectors(
            attractor=self.planet,
            r=self.coordinates,
            v=self.velocity
        )

        self.timeScale = timeScale

    def getOrbitCoordinates(self, points=100) -> list[float]:
        """
        Возвращает координаты точек принадлежащих орбите
        :param points:
        :return: ((x1, y1), (x2, y2), (x3, y3), ...)
        """
        times = linspace(0, self.orbit.period.to(u.s), points)

        positions = [tuple(self.orbit.propagate(time << u.s).r.value)[:2] for time in times]

        return positions

    def getCoordinates(self) -> tuple[float]:
        currTime = time() * u.s - self.lastChangeOfOrbit
        return tuple(self.orbit.propagate(currTime).r.value)[:2]

    def blow(self, thrustVector: tuple, delta_time: float):
        """
        Изменяет значения скорости в точке на орбите
        :param thrustVector:
        :param delta_time:
        :return:
        """
        thrustVector = array(thrustVector)

        delta_time, timeElapsed = delta_time * u.s, (time() - self.lastChangeOfOrbit) * u.s

        deltaInTime = 10 * u.s

        self.coordinates = self.orbit.propagate(timeElapsed)
        nextCoordinates = self.orbit.propagate(timeElapsed + delta_time)

        self.velocity = (nextCoordinates - self.coordinates) / deltaInTime

        thrustVector = thrustVector * u.m / (u.s * u.s)

        gValue = self.planet.k / (linalg.norm(self.coordinates) ** 2)
        rValue = linalg.norm(self.coordinates)

        gOneVector = ((self.coordinates.copy() * -1) / rValue) * gValue

        commonAcceleration = thrustVector + gOneVector

        deltaV = commonAcceleration * delta_time
        self._updateVelocity(deltaV)
        self.lastChangeOfOrbit = time()

    def _updateVelocity(self, delta):
        self.velocity += delta

        self.orbit = Orbit.from_vectors(
            attractor=self.planet,
            r=self.coordinates,
            v=self.velocity
        )
