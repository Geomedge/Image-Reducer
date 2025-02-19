import os
from PIL import Image

def convert(found_files):
        x1 = 350
        for i in range(len(found_files)):
            base_width = x1
            img = Image.open(found_files[i])
            wpercent = (base_width / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)
            img.save()
            

def b():
    found_files = []
    for root, dirs, files in os.walk(r"C:\Users\wiecz\Pictures"):
        for file in files:
            if file.endswith(".jpg"):
                found_files.append(os.path.join(root, file))
    convert(found_files)

b()