from Models.Orbit import Orbit
from numpy import array, linspace, linalg
from poliastro.bodies import *
from astropy import units as u



BODIES = {
    "Earth": Earth,
    "Mercury": Mercury,
    "Moon": Moon,
    "Sun": Sun,
    "Mars": Mars
}


class Station:
    def __init__(self, bodyName: str):

        self.planet = BODIES[bodyName]

        self.coordinates = array(
            [
                403e3 + self.planet.R.value,
                0,
                0
            ]
        ) * u.m

        self.velocity = array(
            [
                0,
                7.33e3,
                0
            ]
        ) * u.m / u.s

        self.orbit = Orbit.from_vectors(
            attractor=self.planet,
            r=self.coordinates,
            v=self.velocity
        )

    def setVelocity(self, x, y):
        self.velocity = array([x, y, 0]) * u.m / u.s
        self.orbit = Orbit.from_vectors(
            attractor=self.planet,
            r=self.coordinates,
            v=self.velocity
        )

    def getOrbitCoordinates(self, points=100):
        times = linspace(0, self.orbit.period.to(u.s), points)

        positions = [self.orbit.propagate(time << u.s).r for time in times]

        x_vals, y_vals, z = zip(*positions)
        x_vals = [val.value for val in x_vals]
        y_vals = [val.value for val in y_vals]

        return x_vals, y_vals

    def getCoordinates(self, inTime: float):
        return self.orbit.propagate(inTime * u.s).r.value,

    def blow(self, thrustVector: array, delta_time: float):
        thrustVector = thrustVector * u.m / (u.s * u.s)
        gValue = self.planet.k / (linalg.norm(self.coordinates) ** 2)
        rValue = linalg.norm(self.coordinates)
        gOneVector = ((self.coordinates.copy() * -1) / rValue.value) * gValue.value
        print(gOneVector)

        deltaV = thrustVector * (delta_time * u.s)

