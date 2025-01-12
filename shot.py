from circleshape import CircleShape
import pygame
import constants

class Shot(CircleShape):
    # class variable
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x,y,constants.SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, color="white", center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt