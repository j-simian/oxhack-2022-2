from levelloader import Level_Loader 
import pygame
import math

class Level:
    def __init__(self, index):
        self.loader = Level_Loader(1)
        self.blocks = self.loader.load_level(1)
        self.bg1 = pygame.image.load("./assets/art/background1.png").convert_alpha()
        self.bg2 = pygame.image.load("./assets/art/background2.png").convert_alpha()
        self.bg3 = pygame.image.load("./assets/art/background3.png").convert_alpha()
        self.player_position = self.loader.player_initial_position(1)
        self.boxes = self.loader.box_initialisation(1)
        print(self.boxes)
        self.radcam = pygame.image.load("./assets/art/background_radcam.png").convert_alpha()
        self.fg = pygame.image.load("./assets/art/lvl1/foreground.png").convert_alpha()
        self.mg = pygame.image.load("./assets/art/lvl1/midground.png").convert_alpha()

    def draw_bg(self, screen, frame):
        bg_img = self.bg1 if (frame // 20) % 3 == 0 else self.bg2 if (frame // 20) % 3 == 1 else self.bg3
        screen.blit(bg_img, (0, 0))
        screen.blit(self.radcam, (0, math.sin(frame / 40)*15))
        # for i in range(0, len(self.blocks)):
        #     for j in range(0, len(self.blocks[i])):
        #         pygame.draw.rect(screen, (255, 0, 255) if self.blocks[i][j] == 1 else (255, 255, 255), pygame.Rect(i*40, j*40, 40, 40), 1)

    def draw_fg(self, screen):
        screen.blit(self.fg, (0, 0))

    def draw_mg(self, screen):
        screen.blit(self.mg, (0, 0))

    @staticmethod
    def pixel_to_tile(x, y):
        return (int(x // 40), int(y // 40))

    @staticmethod
    def tile_to_pixel(x, y):
        return (x * 40, y * 40)
