from PIL import Image #pip install pillow
import numpy as np
image = Image.open("assets/level1/level.png")
image_array = np.array(image)
for each in image_array:
    print(each)