from PIL import Image #pip install pillow

blocks = {
    "00000000": 0, #    AIR
    "000000ff": 1, #    GROUND
    "ff0000ff": 2, #    START   (initial position of player)
    "ffff00ff": 3, #    END     (level won when player gets here)
    "0000ffff": 4, #    BOX     (player-2-controlled box)
    "ff00ffff": 5, #    SPIKE   (kills you)
}

class Level_Loader:
    def __init__(self, index):
        self.level_image = Image.open("assets/lvl_data/lvl"+str(index)+".png").convert("RGBA")

        self.startlocation = (-1,-1)
        self.boxes=[]
        self.level=[]

        for x in range(0, 48):
            level_column=[]
            for y in range(0,27):
                r,g,b,a=(self.level_image.getpixel((x, y)))
                hex_code = hex(r*16**6+g*16**4+b*16**2+a)[2:].zfill(8)
                block=blocks[hex_code]
                if block==2:
                    self.startlocation = (x*40,y*40)
                if block==4:
                    if (x==0 or self.level_image.getpixel((x-1, y))!=(0,0,255,255)) and (y==0 or self.level_image.getpixel((x, y-1))!=(0,0,255,255)):
                        width=1
                        height=1
                        while x+width<48 and self.level_image.getpixel((x+width, y))==(0,0,255,255):
                            width+=1
                        while y+height<27 and self.level_image.getpixel((x, y+height))==(0,0,255,255):
                            height+=1
                        self.boxes+=[(x,y,width,height)]

                level_column+=[block]
            self.level+=[level_column]

    
    def load_level(self,index):
        return(self.level)

    def load_bounding_box(self, index):
        level_bounding_box = Image.open("assets/lvl_data/lvl"+str(index)+"b.png").convert("RGBA")
        level=[]
        for x in range(0, 48):
            level_row=[]
            for y in range(0,27):
                r,g,b,a=(level_bounding_box.getpixel((x, y)))
                if a==0:
                    level_row+=[0]
                else:
                    level_row+=[1]
            level+=[level_row]
        return(level)

    def player_initial_position(self, index):
        return self.startlocation

    def box_initialisation(self, index):
        return self.boxes