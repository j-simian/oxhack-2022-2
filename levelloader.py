from PIL import Image #pip install pillow
import numpy as np
image = Image.open("assets/lvl_data/lvl1.png").convert("RGBA")
level=[]
print("hello?")
for y in range(0, 27):
    level_row=[]
    for x in range(0,48):
        r,g,b,a=(image.getpixel((x, y)))
        if a==0:
            level_row+=[0]
        elif (r,g,b)==(0,0,0):
            level_row+=[1]
        elif (r,g,b)==(255,0,0):
            level_row+=[2]
        elif (r,g,b)==(255,255,0):
            level_row+=[3]
        else:
            print("lol")
    level+=[level_row]

for each in level:
    print(each)


#   KEY:
#   0   =   AIR
#   1   =   GROUND
#   2   =   START   (initial player position)
#   3   =   FINISH  (level ends when player reaches here)