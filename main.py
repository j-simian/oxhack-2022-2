import pygame

(width, height) = (800, 600)

pygame.display.set_caption("minimal program")
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.flip()

def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

game_loop()
