from PIL import Image #pip install pillow

blocks = {
    "00000000": 0, #    AIR
    "000000ff": 1, #    GROUND
    "ff0000ff": 2, #    START   (initial position of player)
    "ffff00ff": 3, #    END     (level won when player gets here)
    "0000ffff": 4, #    BOX     (player-2-controlled box)
    "ff00ffff": 5, #    SPIKE   (kills you)
}

def load_level(index):
    image = Image.open("assets/lvl_data/lvl"+str(index)+".png").convert("RGBA")
    level=[]
    for y in range(0, 27):
        level_row=[]
        for x in range(0,48):
            r,g,b,a=(image.getpixel((x, y)))
            hex_code = hex(r*16**6+g*16**4+b*16**2+a)[2:].zfill(8)
            level_row+=[blocks[hex_code]]
        level+=[level_row]
    return(level)

def load_bounding_box(index):
    image = Image.open("assets/lvl_data/lvl"+str(index)+"b.png").convert("RGBA")
    level=[]
    for y in range(0, 27):
        level_row=[]
        for x in range(0,48):
            r,g,b,a=(image.getpixel((x, y)))
            if a==0:
                level_row+=[0]
            else:
                level_row+=[1]
        level+=[level_row]
    return(level)