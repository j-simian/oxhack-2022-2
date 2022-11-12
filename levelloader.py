from PIL import Image #pip install pillow
import numpy as np
image = Image.open("assets/level1/level.png")
image_array = np.array(image)
print(image_array)