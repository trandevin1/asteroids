from circleshape import CircleShape
import pygame
from constants import *
from random import uniform


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle_1 = uniform(20.0, 50.0)
            vect_1 = self.velocity.rotate(random_angle_1)
            vect_2 = self.velocity.rotate(-random_angle_1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = vect_1 * 1.2
            asteroid2.velocity = vect_2 * 1.2

