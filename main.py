import pygame
import game_objects
import microbit
from PIL import Image
from level import Level

(width, height) = (1920, 1080)

pygame.display.set_caption("oxsplat")
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.flip()

player = game_objects.Player(100, 100)

objects = [player]
keys = []
bit_keys = []
level = Level(1)
clock = pygame.time.Clock()

ROLL = 512
PITCH = 513
BIT_A = 514
BIT_B = 515


def game_loop():
    frame = 0
    running = 1
    roll, pitch = 0, 0
    while running:
        keys=pygame.key.get_pressed()

        # roll, pitch, a, b = microbit.bitman(roll, pitch)
        # bit_keys=(roll, pitch, a, b)
        bit_keys = ()

        # render
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 0, width, height))
        level.draw_bg(screen, frame)
        for i in objects:
            i.tick(level.blocks, { "keys": keys, "microbit": bit_keys })
        for i in objects:
            i.render(screen)
        level.draw_mg(screen)
        level.draw_fg(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0
        clock.tick(60)
        frame += 1





game_loop()
