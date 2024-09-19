from circleshape import CircleShape
import pygame
from constants import *
from random import uniform


class Explosion(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "lightblue", self.position, self.radius, 100)

    def update(self, dt):
        self.position += self.velocity * dt

    def spawn(self, position):
        random_angle_1 = uniform(20.0, 50.0)
        random_angle_2 = uniform(180, 210)
        vect_1 = self.velocity.rotate(random_angle_1)
        vect_2 = self.velocity.rotate(-random_angle_1)
        vect_3 = self.velocity.rotate(random_angle_2)
        vect_4 = self.velocity.rotate(-random_angle_2)
        particle1 = Explosion(position.x, position.y, EXPLOSION_RADIUS)
        particle2 = Explosion(position.x, position.y, EXPLOSION_RADIUS)
        particle3 = Explosion(position.x, position.y, EXPLOSION_RADIUS)
        particle4 = Explosion(position.x, position.y, EXPLOSION_RADIUS)
        particle1.velocity
