from levelloader import Level_Loader
import pygame
import math
import random

levelWon = False
dead = False

class Level:
    def __init__(self, levelnumber):
        self.level_index = levelnumber
        self.level_menu = pygame.image.load("./assets/startscreens/lvl" + str(self.level_index) + "n.png").convert_alpha()
        self.loader = Level_Loader(self.level_index)
        self.blocks = self.loader.load_level(self.level_index)
        self.bounding_boxes = self.loader.load_bounding_box(self.level_index)
        self.bg1 = pygame.image.load("./assets/art/background1.png").convert_alpha()
        self.bg2 = pygame.image.load("./assets/art/background2.png").convert_alpha()
        self.bg3 = pygame.image.load("./assets/art/background3.png").convert_alpha()
        self.player_position = self.loader.player_initial_position(self.level_index)
        self.boxes = self.loader.box_initialisation(self.level_index)
        self.radcam = pygame.image.load("./assets/art/background_radcam.png").convert_alpha()
        self.fg = pygame.image.load("./assets/art/lvl" + str(self.level_index) + "/foreground.png").convert_alpha()
        self.mg = pygame.image.load("./assets/art/lvl" + str(self.level_index) + "/midground.png").convert_alpha()
        self.stars = []
        self.starx = 960
        self.stary = -100
        for i in range(0, 4):
            self.stars += [pygame.image.load("./assets/art/shooting_star_" + str(i+1) + ".png").convert_alpha()]
        self.currstars = []

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

    def add_star(self):
        self.currstars += [[random.choice(self.stars), random.uniform(760, 1060), -100, False]]


    def render_star(self, screen, frame):
        for i in self.currstars:
            i[1] -= 2
            i[2] += 2
            screen.blit(i[0], (i[1], i[2]))
            if i[2] > 1080:
                i[3] = True
        self.currstars = filter(lambda x: not x[3], self.currstars)


    @staticmethod
    def pixel_to_tile(x, y):
        return (int(x // 40), int(y // 40))

    @staticmethod
    def tile_to_pixel(x, y):
        return (x * 40, y * 40)
