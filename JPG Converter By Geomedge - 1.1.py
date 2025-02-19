from PIL import Image
import os
import glob

def function1(name):
    base_width = 400
    img = Image.open(name)
    wpercent = (base_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)
    img.save(name)
    print(f"Shrunk {name}")




for name in glob.glob('C:/Users/Robert Wieczorek/Desktop/Images/*/*/*.jpg'):
    function1(name)