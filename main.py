import pygame

(width, height) = (800, 600)

pygame.display.set_caption("minimal program")
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.flip()

def game_loop():
    running = True
    while running:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, width, height))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

game_loop()
