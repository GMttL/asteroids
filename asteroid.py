from circleshape import CircleShape
import pygame
import constants
import random


class Asteroid(CircleShape):
    # class variable
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, color="white", center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius < constants.ASTEROID_MIN_RADIUS:
            return

        spawn_angle = random.uniform(20, 50)
        plus_vec = self.velocity.rotate(spawn_angle)
        minus_vec = self.velocity.rotate(-spawn_angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        smaller_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        smaller_asteroid_1.velocity = plus_vec * 1.2

        smaller_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        smaller_asteroid_2.velocity = minus_vec * 1.2
        