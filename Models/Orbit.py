from numpy import array, linalg, arccos
from math import degrees, radians, sin, cos
from Models.Planet import Planet


class Orbit:
    apogee: float = 1.5e9
    perigee: float = 1.5e9
    angle: float = 270
    eccentricity: float = 0
    planet = Planet(6.4e6, 6e24)

    '''
    def calculateOrbit(self, velocityVector: array, heightVector: array, velocity):
        heightVectorLength = linalg.norm(heightVector)

        r = heightVectorLength + self.planet.radius
        print(r)
        mu = self.planet.getMU()
        print(mu)
        phi = arccos(velocityVector.dot(heightVector) /
                     (linalg.norm(velocityVector) * r)
                     )
        tangentVelocity = sin(phi) * velocity
        angularMomentum = tangentVelocity * heightVectorLength

        axisA = 1 / ((2 / r) - (velocity ** 2 / mu))
        p = angularMomentum * angularMomentum / mu
        e = (1 - (angularMomentum * angularMomentum / (mu * axisA))) ** 0.5

        return axisA, e '''


