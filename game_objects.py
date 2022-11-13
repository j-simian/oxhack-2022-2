import pygame
from PIL import Image
from level import Level, levelWon

class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vely = 0
        self.velx = 0
        self.velxd = 0
        self.velyd = 0
        self.gravity = False
        self.collision = True
        self.touches_ground = False
        self.alive=True

    def render(self, screen, frame):
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x, self.y, 16, 32))

    def tick(self, level, ins, objects):
        if self.alive==False: return 2

        blocks=level.blocks

        if self.gravity:
            self.vely = min(18, self.vely+0.7)

        if self.collision:
            
            for each in objects:
                if isinstance(each, Controllable_Box):
                    if self.x+self.w <= each.x and self.x+self.w + self.velx > each.x and self.y + self.h > each.y and self.y < each.y + each.h: #rightwards
                        self.velx = 0
                        self.x = each.x - self.w - 1
                    if self.x >= each.x+each.w and self.x + self.velx < each.x+each.w and self.y + self.h > each.y and self.y < each.y + each.h: #leftwards
                        self.velx = 0
                        self.x = each.x+each.w+1
                    if self.y + self.h < each.y + 40 and self.y + self.h > each.y and self.x <= each.x+each.w and self.x + self.w >= each.x: #downwards - should there be a self.vely in here???
                        self.vely=max(0,each.vely)
                        self.y = each.y - self.h
                    if self.y >= each.y + each.h and self.y + self.vely < each.y + each.h and self.x <= each.x+each.w and self.x + self.w >= each.x: #upwards
                        self.vely = 0
                        self.y = each.y + each.h+1
            for i in range(0, len(blocks)):
                for j in range(0, len(blocks[i])):

                    collide = False
                    if blocks[i][j] not in [1,3,5]:
                        continue
                    pixel = Level.tile_to_pixel(i, j)
                    if self.x+self.w <= pixel[0] and self.x+self.w + self.velx + self.velxd > pixel[0] and self.y + self.h > pixel[1] and self.y < pixel[1] + 40: #rightwards
                        collide = True
                        self.velx = 0
                        self.velxd = 0
                        self.x = pixel[0] - self.w - 1
                    if self.x >= pixel[0]+40 and self.x + self.velx + self.velxd < pixel[0]+40 and self.y + self.h > pixel[1] and self.y < pixel[1] + 40: #leftwards
                        collide = True
                        self.velx = 0
                        self.velxd = 0
                        self.x = pixel[0]+41
                    if self.y + self.h <= pixel[1] and self.y + self.vely + self.velyd + self.h > pixel[1] and self.x <= pixel[0]+40 and self.x + self.w >= pixel[0]: #downwards
                        collide = True
                        self.vely = 0
                        self.velyd = 0
                        self.y = pixel[1] - self.h
                    if self.y >= pixel[1] + 40 and self.y + self.vely + self.velyd < pixel[1] + 40 and self.x <= pixel[0]+40 and self.x + self.w >= pixel[0]: #upwards
                        collide = True
                        self.vely = 0
                        self.velyd = 0
                        self.y = pixel[1] + 41
                    if collide and blocks[i][j] == 3:
                        return 1

                    if collide and blocks[i][j] == 5:
                        return 2

        self.y += self.vely
        self.x += self.velx
        return 0

class Controllable_Box(GameObject):
    def __init__(self, x, y, w, h, levelnumber):
        super(Controllable_Box, self).__init__(x*40, y*40)
        self.w = w*40
        self.h = h*40
        self.gravity = False
        self.collision = False
        self.velx = 0
        self.me = pygame.image.load("./assets/art/lvl" + str(levelnumber) + "/moveblock.png").convert_alpha()

    def render(self, screen, frame):
        screen.blit(self.me, (self.x - 28, self.y - 19))

    def tick(self, level, ins, objects):
        super(Controllable_Box, self).tick(level, ins, objects)

        roll = ins["microbit"][0]
        pitch= ins["microbit"][1]
        if roll<-5:
            tiltx=max(5+roll,-60)
        elif roll>5:
            tiltx=min(-5+roll,60)
        else:
            tiltx=0
        
        if pitch<-5:
            tilty=max(5+pitch,-60)
        elif pitch>5:
            tilty=min(-5+pitch,60)
        else:
            tilty=0
        self.velx = min((tiltx/4 + self.velx) / 2, 40)
        self.vely = min((tilty/4 + self.vely) / 2, 40)


        blocks=level.bounding_boxes
        for i in range(0, len(blocks)):
            for j in range(0, len(blocks[i])):
                if blocks[i][j] == 1:
                    continue
                pixel = Level.tile_to_pixel(i, j)
                if self.x+self.w <= pixel[0] and self.x+self.w + self.velx > pixel[0] and self.y + self.h > pixel[1] and self.y < pixel[1] + 40: #rightwards
                    self.velx = 0
                    self.x = pixel[0] - self.w - 1
                if self.x >= pixel[0]+40 and self.x + self.velx < pixel[0]+40 and self.y + self.h > pixel[1] and self.y < pixel[1] + 40: #leftwards
                    self.velx = 0
                    self.x = pixel[0]+41
                if self.y + self.vely + self.h < pixel[1] + 41 and self.y + self.vely + self.h > pixel[1] and self.x <= pixel[0]+40 and self.x + self.w >= pixel[0]: #downwards
                    self.vely = 0
                    self.y = pixel[1] - self.h - 1
                if self.y >= pixel[1] + 40 and self.y + self.vely < pixel[1] + 40 and self.x <= pixel[0]+40 and self.x + self.w >= pixel[0]: #up
                    self.vely = 0
                    self.y = pixel[1] + 41
        self.x=min(self.x,1920-self.w)
        self.x=max(self.x,0)
        self.y=min(self.y,1080-self.h)
        self.y=max(self.y,0)

        for each in objects:
            if isinstance(each, Player): #push player around
                if self.x+self.w <= each.x and self.x+self.w + self.velx > each.x and self.y + self.h > each.y and self.y < each.y + each.h: #rightwards
                    each.velx = max(each.velx,self.velx)
                    each.x = self.x + self.w + 1
                if self.x >= each.x+each.w and self.x + self.velx < each.x+each.w and self.y + self.h > each.y and self.y < each.y + each.h: #leftwards
                    each.velx = min(each.velx,self.velx)
                    each.x = self.x-each.w-1
                if self.y + self.h < each.y + 40 and self.y + self.h > each.y and self.x <= each.x+each.w and self.x + self.w >= each.x: #downwards
                    each.vely = max(each.vely,self.vely)
                    each.y = self.y + self.h + 1
                # if (self.y >= each.y + each.h and self.y + self.vely < each.y + each.h and self.x <= each.x+each.w and self.x + self.w >= each.x): #not upwards
                #     each.vely = min(each.vely,self.vely)
                #     each.y = self.y - self.h - 1
                blocks=level.blocks #test if player is now in a box
                for i in range(0, len(blocks)):
                    for j in range(0, len(blocks[i])):
                        if blocks[i][j] != 1:
                            continue
                        pixel = Level.tile_to_pixel(i, j)
                        x1=each.x
                        y1=each.y
                        x2=x1+each.w
                        y2=y1+each.h

                        x3=pixel[0]
                        y3=pixel[1]
                        x4=x3+40
                        y4=y3+40
                        if (x1+20<x4)and(x3+20<x2)and(y1+20<y4)and(y3+20<y2):
                            each.alive=False

                        x5=self.x
                        y5=self.y
                        x6=x5+self.w
                        y6=y5+self.h
                        if (x1+20<x6)and(x5+20<x2)and(y1+20<y6)and(y5+20<y2):
                            each.alive=False


class Player(GameObject):
    def __init__(self, x, y):
        super(Player, self).__init__(x, y)
        self.w = 40
        self.h = 80
        self.gravity = True
        self.touches_box = False
        self.stand = pygame.image.load("./assets/art/sprite/stand.png").convert_alpha()
        self.jumpur = pygame.image.load("./assets/art/sprite/jump up right.png").convert_alpha()
        self.jumpul = pygame.image.load("./assets/art/sprite/jump up left.png").convert_alpha()
        self.jumpdr = pygame.image.load("./assets/art/sprite/jump down right.png").convert_alpha()
        self.jumpdl = pygame.image.load("./assets/art/sprite/jump down left.png").convert_alpha()
        self.walkr = [pygame.image.load("./assets/art/sprite/right walk 1.png").convert_alpha(), pygame.image.load("./assets/art/sprite/right walk 2.png").convert_alpha(), pygame.image.load("./assets/art/sprite/right walk 3.png").convert_alpha(), pygame.image.load("./assets/art/sprite/right walk 4.png").convert_alpha()]
        self.walkl = [pygame.image.load("./assets/art/sprite/left walk 1.png").convert_alpha(), pygame.image.load("./assets/art/sprite/left walk 2.png").convert_alpha(), pygame.image.load("./assets/art/sprite/left walk 3.png").convert_alpha(), pygame.image.load("./assets/art/sprite/left walk 4.png").convert_alpha()]
        self.state = self.stand
        self.velxd = 0
        self.velyd = 0

    def render(self, screen, frame):
        if self.state == self.walkl or self.state == self.walkr:
            screen.blit(self.state[(int(frame / 10)) % 4], (self.x - 22, self.y - 15))
        else:
            screen.blit(self.state, (self.x - 22, self.y - 15))

    def tick(self, level, ins, objects):
        if abs(self.velx) < 1 and (self.touches_ground or self.touches_box):
            self.state = self.stand

        if not (self.touches_box and self.touches_ground):
            self.velxd /= 1.05
            self.velyd /= 1.05
        player_tile = Level.pixel_to_tile(self.x, self.y)
        self.touches_box = False
        if player_tile[0] > 46 or player_tile[0] < 0 or player_tile[1] > 26 or player_tile[1] < 0:
            pass
        elif level.blocks[player_tile[0]][player_tile[1] + 2] == 1 or level.blocks[player_tile[0]+1][player_tile[1]+2] == 1:
            self.touches_ground = True
        else:
            self.touches_ground = False
            for i in objects:
                if isinstance(i, Controllable_Box):
                    if self.x <= i.x + i.w and self.x >= i.x - self.w and i.y - self.y - self.h <= 2 and i.y - self.y - self.h > -79 + self.velyd:
                        self.touches_box = True
                        self.velxd = i.velx
                        self.velyd = i.vely
                        break

        if self.state == self.jumpul and self.vely > 0:
            self.state = self.jumpdl
        if self.state == self.jumpur and self.vely > 0:
            self.state = self.jumpdr
    
        
        ret = super(Player, self).tick(level, ins, objects)
        if ret == 1:
            return 1
        elif ret == 2:
            return 2

        self.x += self.velxd
        self.y += min(self.velyd, 0)



        self.handle_input(ins)

    def handle_input(self, ins):
        left, right = False, False
        if self.velx > -10 and ins["keys"][pygame.K_a]:
            left = True
        if self.velx < 10 and ins["keys"][pygame.K_d]:
            right = True

        if left:
            self.velx = max(self.velx - 2, -12)
            if self.touches_ground or self.touches_box:
                self.state = self.walkl
            else:
                if self.vely > 0:
                    self.state = self.jumpdl
                elif self.vely < 0:
                    self.state = self.jumpul
        if right:
            self.velx = min(self.velx + 2, 12)
            if self.touches_ground or self.touches_box:
                self.state = self.walkr
            else:
                if self.vely > 0:
                    self.state = self.jumpdr
                elif self.vely < 0:
                    self.state = self.jumpur
        if ((not left and not right) or (left and right)):
            if self.touches_ground or self.touches_box:
                self.velx /= 1.8
            else:
                self.velx /= 1.05
        if ins["keys"][pygame.K_w] and (self.touches_ground or self.touches_box):
            self.vely = -15
            self.state = self.jumpul
            self.velyd *= 2
            self.velxd *= 2
