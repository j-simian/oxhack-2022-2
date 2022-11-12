import pygame



class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vely = 0
        self.velx = 0
        self.w = 16
        self.h = 32

    def render(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, 16, 32))

    def tick(self):
        self.y += self.vely
        self.x += self.velx
        self.vely = max(2, self.vely+0.2)

