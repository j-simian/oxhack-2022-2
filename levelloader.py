from PIL import Image #pip install pillow
import numpy as np

blocks = {
    "00000000": 0, #    AIR
    "000000ff": 1, #    GROUND
    "ff0000ff": 2, #    START   (initial position of player)
    "ffff00ff": 3, #    END     (level won when player gets here)
    "0000ffff": 4, #    BOX     (player-2-controlled box)
}

def load_level(index_string):
    image = Image.open("assets/lvl_data/lvl"+index_string+".png").convert("RGBA")
    level=[]
    print("hello?")
    for y in range(0, 27):
        level_row=[]
        for x in range(0,48):
            r,g,b,a=(image.getpixel((x, y)))
            hex_code = hex(r*16**6+g*16**4+b*16**2+a)[2:].zfill(8)
            print(hex_code)
            level_row+=[blocks[hex_code]]
        level+=[level_row]
    return(level)

for each in load_level("1"):
    print(each)


#   KEY:
#   0   =   AIR
#   1   =   GROUND
#   2   =   START   (initial player position)
#   3   =   FINISH  (level ends when player reaches here)