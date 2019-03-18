import os
import shutil
from unrar import rarfile

path = os.getcwd()
allFile = os.listdir(path)

for dir in allFile:
    if os.path.isdir(dir):
        os.chdir(dir)
        dir2 = os.listdir()
        for file in dir2:
            if '.rar' in file:
                rar = rarfile.RarFile(file)
                rar.extractall(path)
                os.remove(file)
                print(f'删除文件{file}成功')
        os.chdir('..')