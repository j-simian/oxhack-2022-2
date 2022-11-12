import pygame
import game_objects
from PIL import Image

(width, height) = (1920, 1080)

pygame.display.set_caption("minimal program")
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.flip()

player = game_objects.Player(100, 100)

objects = [player]

def game_loop():
    running = True
    while running:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, width, height))
        draw_bg(screen)
        for i in objects:
            i.tick()
        for i in objects:
            i.render(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


game_loop()
