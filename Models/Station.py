import time
from typing import Collection, Any

from numpy import array, ndarray
from math import sin, cos
from Models.Planet import Planet
from Models.Orbit import Orbit


class Station:
    name = "James Webb Telescope"
    planet = Planet(6.4e6, 6e24)
    height_vector: ndarray[float] = array([408e3 + planet.radius, 0])
    velocity: float = 7.66e3
    throttle: float = 0
    maxThrottle = 4
    heading_vector: ndarray[float] = array([velocity, 90])
    throttle_vector: ndarray[float] = array([throttle * maxThrottle, 90])
    orbit: Orbit
    last_update: float = 0

    def __init__(self):
        self.orbit = Orbit()

    def get_position(self):
        return (self.height_vector[0] * cos(self.height_vector[1]),
                self.height_vector[0] * sin(self.height_vector[1]))

    def get_angular_velocity(self) -> float:
        return self.heading_vector[0] / self.height_vector[0]

    def update_angle(self, delta_time: float) -> None:
        delta_angle = self.get_angular_velocity() * delta_time
        self.heading_vector[1] += delta_angle
        self.height_vector[1] += delta_angle

    def update(self):
        now = time.time()*100
        delta_time = now - self.last_update
        self.update_angle(delta_time)
        self.last_update = now