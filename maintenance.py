# Setup Python ----------------------------------------------- #
import shutil
import os

from pygame import image, transform
# Funcs ------------------------------------------------------ #
def load_image(path):
    temp = image.load(path).convert_alpha()
    surface = transform.scale(temp, (temp.get_width() * 2, temp.get_height() * 2))
    del temp
    return surface

def console_push(message):
    print(message)

def clear_project():
    try:
        location = "./"
        dir = "__pycache__"

        path = os.path.join(location, dir)

        shutil.rmtree(path)
    except:
        print("Main cache could not be removed")
    
    try:
        location = "./loops"
        dir = "__pycache__"

        path = os.path.join(location, dir)

        shutil.rmtree(path)
    except:
        print("loops cache could not be removed")