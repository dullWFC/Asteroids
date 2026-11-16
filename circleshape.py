import pygame

from constants import *


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pass

    def update(self, dt: float) -> None:
        # must override
        pass

    def collides_with(self, other) -> bool:
        radius = self.radius + other.radius
        distance = self.position.distance_to(other.position)
        return distance <= radius

    def warp(self):
        if self.position.x > SCREEN_WIDTH + 80:
            self.position.x = 0
        elif self.position.x < -80:
            self.position.x = SCREEN_WIDTH

        if self.position.y > SCREEN_HEIGHT + 80:
            self.position.y = 0
        elif self.position.y < -80:
            self.position.y = SCREEN_HEIGHT
