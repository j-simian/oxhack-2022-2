import pygame
import game_objects

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
        for i in objects:
            objects.tick()
        for i in objects:
            objects.render(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

game_loop()
