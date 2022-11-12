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

    def tick(self, level, keys):
        if self.gravity:
            self.vely = min(18, self.vely+0.7)

        if self.collision:
            for i in range(0, len(level)):
                for j in range(0, len(level[i])):
                    if level[i][j] != 1:
                        continue
                    pixel = Level.tile_to_pixel(i, j)
                    if self.x+self.w <= pixel[0] and self.x+self.w + self.velx > pixel[0] and self.y + self.h > pixel[1] and self.y < pixel[1] + 40: #rightwards
                        self.velx = 0
                        self.x = pixel[0] - self.w - 1
                    if self.x >= pixel[0]+40 and self.x + self.velx < pixel[0]+40 and self.y + self.h > pixel[1] and self.y < pixel[1] + 40: #leftwards
                        self.velx = 0
                        self.x = pixel[0]+41
                    if self.y + self.h <= pixel[1] and self.y + self.vely + self.h > pixel[1] and self.x <= pixel[0]+40 and self.x + self.w >= pixel[0]: #downwards
                        self.vely = 0
                        self.y = pixel[1] - self.h
                    if self.y >= pixel[1] + 40 and self.y + self.vely < pixel[1] + 40 and self.x <= pixel[0]+40 and self.x + self.w >= pixel[0]: #downwards
                        self.vely = 0
                        self.y = pixel[1] + 41
                    # if self.y >= pixel[1]+40 and self.y + self.vely < pixel[1]+40: #upwards
                    #     self.vely = 0
                    #     self.y = pixel[1]+40
        self.y += self.vely
        self.x += self.velx

class Player(GameObject):
    def __init__(self, x, y):
        super(Player, self).__init__(x, y)
        self.w = 40
        self.h = 80
        self.gravity = True

    def render(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, self.w, self.h))

    def tick(self, level, keys):
        super(Player, self).tick(level, keys)
        player_tile = Level.pixel_to_tile(self.x, self.y)
        if level[player_tile[0]][player_tile[1] + 2] == 1 or level[player_tile[0]+1][player_tile[1]+2] == 1:
            self.touches_ground = True
        else:
            self.touches_ground = False
        self.handle_input(keys)

    def handle_input(self, keys):
        if keys[pygame.K_a]:
            self.velx = max(self.velx - 2, -15)
        if keys[pygame.K_d]:
            self.velx = min(self.velx + 2, 15)
        if not keys[pygame.K_d] and not keys[pygame.K_a]:
            self.velx = self.velx / 1.8
        if keys[pygame.K_w] and self.touches_ground:
            self.vely = -15
        if keys[pygame.K_e]:
            self.vely = -15
