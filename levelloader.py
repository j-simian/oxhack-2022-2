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

        self.level=[]
        for y in range(0, 27):
            level_row=[]
            for x in range(0,48):
                r,g,b,a=(self.level_image.getpixel((x, y)))
                hex_code = hex(r*16**6+g*16**4+b*16**2+a)[2:].zfill(8)
                block=blocks[hex_code]
                if block==2:
                    self.startlocation = (x*40,y*40)
                level_row+=[block]
            self.level+=[level_row]

    
    def load_level(self,index):
        return(self.level)

    def load_bounding_box(self, index):
        level_bounding_box = Image.open("assets/lvl_data/lvl"+str(index)+"b.png").convert("RGBA")
        level=[]
        for y in range(0, 27):
            level_row=[]
            for x in range(0,48):
                r,g,b,a=(level_bounding_box.getpixel((x, y)))
                if a==0:
                    level_row+=[0]
                else:
                    level_row+=[1]
            level+=[level_row]
        return(level)

    def player_initial_position(self, index):
        return self.startlocation