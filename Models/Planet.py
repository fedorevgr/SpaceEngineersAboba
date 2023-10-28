from scipy.constants import G


class Planet:
    radius: float
    mass: float
    gravitational_parameter: float
    x: int = 0
    y: int = 0

    def __init__(self, radius: float, mass: float) -> None:
        self.radius = radius
        self.mass = mass
        self.gravitational_parameter = radius * mass

    def getMU(self):
        return G * self.mass


        