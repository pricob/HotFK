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
        print("Cache could not be removed")