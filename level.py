import levelloader
import pygame

class Level:
    def __init__(self, index):
        self.blocks = levelloader.load_level("1")
        self.bg_img = pygame.image.load("./assets/lvl_data/lvl" + str(index) + ".png")
        self.bg_img = pygame.transform.scale(self.bg_img, (640, 640))
        # self.bg_img = pygame.image.load("./test/level_graphics_test.png")


    
    def draw_bg(self, screen):
        screen.blit(self.bg_img, (0, 0))

    @staticmethod
    def pixel_to_tile(x, y):
        return (x // 40, y // 40)

    @staticmethod
    def tile_to_pixel(x, y):
        return (x * 40, y * 40)
