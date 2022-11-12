import pygame
from PIL import Image

blocks = {
    "FF0000": "air"
}

u(r, 16) + str(g, 16) + str(b, 16) + str(a, 16)

class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vely = 0
        self.velx = 0
        self.gravity = False

    def render(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x, self.y, 16, 32))

    def tick(self):
        self.y += self.vely
        self.x += self.velx
        if self.gravity:
            self.vely = max(2, self.vely+0.2)

class Player(GameObject):
    def __init__(self, x, y):
        super(Player, self).__init__(x, y)
        self.w = 16
        self.h = 32
        self.gravity = True

    def render(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, self.w, self.h))

    def tick(self):
        super(Player, self).tick()
