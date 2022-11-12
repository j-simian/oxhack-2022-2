import levelloader

class Level:
    def __init__(index):
        self.blocks = levelloader.load_level("1")
        self.bg_img = pygame.image.load("./assets/lvl_data/lvl" + str(index) + ".png")

    def draw_bg(self):
        screen.blit(self.bg_img, (0, 0))
