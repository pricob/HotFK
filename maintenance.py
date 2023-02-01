# Setup Python ----------------------------------------------- #
import shutil
import os

# Funcs ------------------------------------------------------ #
def build():
    pass

def clear_project():
    try:
        location = "./"
        dir = "__pycache__"

        path = os.path.join(location, dir)

        shutil.rmtree(path)
    except:
        print("Main cache could not be removed")
    
    try:
        location = "./classes"
        dir = "__pycache__"

        path = os.path.join(location, dir)

        shutil.rmtree(path)
    except:
        print("Class cache could not be removed")