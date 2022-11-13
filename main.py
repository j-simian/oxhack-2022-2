import pygame
import game_objects
import microbit
from PIL import Image
from level import Level, levelWon, dead

(width, height) = (1920, 1080)


pygame.display.set_caption("City of Dreaming Spires")
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.flip()


levelnumber = 4
objects = []
keys = []
bit_keys = []
level = Level(levelnumber)
player = game_objects.Player(level.player_position[0], level.player_position[1]-40)
objects+=[player]
for each in level.boxes:
    objects+=[game_objects.Controllable_Box(each[0],each[1],each[2],each[3], levelnumber)]
clock = pygame.time.Clock()

ROLL = 512
PITCH = 513
BIT_A = 514
BIT_B = 515


def game_loop():
    global level, objects, levelWon, levelnumber, dead
    frame = 0
    running = 1
    roll, pitch = 0, 0
    while running:
        while not levelWon:
            keys=pygame.key.get_pressed()

            bit_keys = ()
            roll, pitch, a, b = microbit.bitman(roll, pitch)
            bit_keys=(roll, pitch, a, b)

            # render
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 0, width, height))
            level.draw_bg(screen, frame)
            level.shooting_stars(screen, frame)
            level.draw_mg(screen)
            for i in objects:
                state = i.tick(level, { "keys": keys, "microbit": bit_keys }, objects)
                if state == 1:
                    levelWon = True
                    continue
                elif state == 2:
                    dead = True
                    continue
            if levelWon or dead:
                continue
            for i in objects:
                i.render(screen, frame)
            level.draw_fg(screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = 0; exit()
            clock.tick(60)
            frame += 1
        print('WINWINWC')
        
        if levelWon: levelnumber += 1
        level = Level(levelnumber)
        player = game_objects.Player(100, 100)
        objects = [player]
        levelWon, dead = False
        for each in level.boxes:
            objects+=[game_objects.Controllable_Box(each[0],each[1],each[2],each[3], levelnumber)]





game_loop()
