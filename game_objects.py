import pygame
from PIL import Image
from level import Level

class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vely = 0
        self.velx = 0
        self.gravity = False
        self.collision = True

    def render(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x, self.y, 16, 32))

    def tick(self, level):
        if self.gravity:
            self.vely = max(5, self.vely+0.2)
        if self.collision:
            for i in range(0, len(level)):
                for j in range(0, len(level[i])):
                    if level[i][j] == 1:
                        pixel = Level.tile_to_pixel(i, j)
                        if self.x < pixel[0] and self.x + self.velx >= pixel[0]:
                            self.velx = 0
                            self.x = pixel[0]
                        if self.x > pixel[0]+40 and self.x + self.velx <= pixel[0]+40:
                            self.velx = 0
                            self.x = pixel[0]+40
                        if self.y < pixel[1] and self.y + self.vely >= pixel[1]:
                            self.vely = 0
                            self.y = pixel[1]
                        if self.y > pixel[1]+40 and self.y + self.vely <= pixel[1]+40:
                            self.vely = 0
                            self.y = pixel[1]+40
                            print("hi")
        self.y += self.vely
        self.x += self.velx



class Player(GameObject):
    def __init__(self, x, y):
        super(Player, self).__init__(x, y)
        self.w = 16
        self.h = 32
        self.gravity = True

    def render(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, self.w, self.h))

    def tick(self, level):
        super(Player, self).tick(level)
