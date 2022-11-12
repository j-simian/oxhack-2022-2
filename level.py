from levelloader import Level_Loader 
import pygame

class Level:
    def __init__(self, index):
        self.loader = Level_Loader(1)
        self.blocks = self.loader.load_level(1)
        self.bg_img = pygame.image.load("./assets/art/background_stars.png").convert_alpha()
        self.radcam = pygame.image.load("./assets/art/background_radcam.png").convert_alpha()
        self.level = pygame.transform.scale(pygame.image.load("./assets/lvl_data/lvl1.png").convert_alpha(), (1920, 1080))

    def draw_bg(self, screen):
        screen.blit(self.bg_img, (0, 0))
        screen.blit(self.radcam, (0, 20))
        screen.blit(self.level, (0, 0))
        # for i in range(0, len(self.blocks)):
        #     for j in range(0, len(self.blocks[i])):
        #         pygame.draw.rect(screen, (255, 0, 255) if self.blocks[i][j] == 1 else (255, 255, 255), pygame.Rect(i*40, j*40, 40, 40), 1)

    @staticmethod
    def pixel_to_tile(x, y):
        return (int(x // 40), int(y // 40))

    @staticmethod
    def tile_to_pixel(x, y):
        return (x * 40, y * 40)
