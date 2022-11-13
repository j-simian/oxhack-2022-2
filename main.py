import pygame
import game_objects
import microbit
from PIL import Image
from level import Level, levelWon, dead
from random import randint

(width, height) = (1920, 1080)


pygame.display.set_caption("City of Dreaming Spires")
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.flip()


levelnumber = 1
objects = []
keys = []
bit_keys = []
level = Level(levelnumber)
player = game_objects.Player(level.player_position[0], level.player_position[1])
objects=[player]
for each in level.boxes:
    objects+=[game_objects.Controllable_Box(each[0],each[1],each[2],each[3], levelnumber)]
clock = pygame.time.Clock()
start = False

death_counter = 0

ROLL = 512
PITCH = 513
BIT_A = 514
BIT_B = 515


def game_loop():
    global level, objects, levelWon, levelnumber, dead, start, death_counter
    frame = 0
    running = 1
    roll, pitch = 0, 0
    alpha = 0
    death1 = pygame.image.load("./assets/startscreens/death1.png").convert_alpha()
    death2 = pygame.image.load("./assets/startscreens/death2.png").convert_alpha()
    death3 = pygame.image.load("./assets/startscreens/death3.png").convert_alpha()
    death4 = pygame.image.load("./assets/startscreens/death4.png").convert_alpha()
    while running:

        while not (levelWon or dead):   

            keys=pygame.key.get_pressed()             

            bit_keys = ()
            roll, pitch, a, b = microbit.bitman(roll, pitch)
            bit_keys=(roll, pitch, a, b)

            if not start:
                image = level.level_menu
                if alpha < 253: alpha += 2
                screen.fill((0,0,0))    
                image.set_alpha(alpha)    
                screen.blit(image, [0,0])

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        start = True
                    elif event.type == pygame.QUIT:
                        running = 0; exit()

            else:
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
                        alpha = 255
                        rand = randint(1,100)
                        if rand <= 33: image = death1
                        elif rand <= 66: image = death2
                        elif rand <= 99: image = death3
                        else: image = death4
                        death_counter += 1
                        continue
                if levelWon or dead:
                    continue
                for i in objects:
                    i.render(screen, frame)
                level.draw_fg(screen)
                if alpha > 0: 
                    alpha = max(0, alpha -5)  
                    image.set_alpha(alpha)    
                    screen.blit(image, [0,0])

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = 0; exit()
            clock.tick(60)
            frame += 1

        
        if levelWon: 
            levelnumber += 1
            start = False
            level = Level(levelnumber)
        player = game_objects.Player(level.player_position[0], level.player_position[1])
        objects = [player]
        levelWon, dead = False, False
        for each in level.boxes:
            objects+=[game_objects.Controllable_Box(each[0],each[1],each[2],each[3], levelnumber)]





game_loop()
