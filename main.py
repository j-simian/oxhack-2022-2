import pygame
import game_objects
from PIL import Image
from level import Level

(width, height) = (1920, 1080)

pygame.display.set_caption("oxsplat")
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.flip()

player = game_objects.Player(100, 500)

objects = [player]
keys = []
level = Level(1)

def game_loop():
    running = True
    while running:
        keys=pygame.key.get_pressed()

        # render
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, width, height))
        level.draw_bg(screen)
        for i in objects:
            i.tick(level.blocks, keys)
        for i in objects:
            i.render(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False





game_loop()
