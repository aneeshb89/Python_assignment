import os
import shutil


def backup(path, bckup):
    os.chdir(path)
    dir = os.listdir(path)

    print(dir)
    
    for file in dir:
     shutil.copy(file, bckup)

path = "E:\\source"
bckup = "E:\\python_backup"  
backup(path, bckup)
