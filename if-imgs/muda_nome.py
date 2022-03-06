from PIL import Image
import os

path = os.getcwd()

l, t, r, b = 0, 26, 1008, 731

for i in range(1,28):
    im = Image.open(f"{os.getcwd()}\\img{i}.png")
    im1 = im.crop((l, t, r, b))
    im1.save(f"img{i}.png")
