# Setup Python ----------------------------------------------- #
import shutil
import os

# Funcs ------------------------------------------------------ #
def build():
    pass

def clear_project():
    location = "./"
    dir = "__pycache__"

    path = os.path.join(location, dir)

    shutil.rmtree(path)