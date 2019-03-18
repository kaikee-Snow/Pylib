# coding:utf-8
# !/usr/bin/env python

import os
import sys
import tarfile
version = sys.version_info
if version.major == 2:
    print("Python has been installed")
    print("Python version is %d.%d" % (version.major, version.minor))
elif version.major == 3:
    print("Python has been installed.")
    print(f"Python version is {version.major}.{version.minor}")
else:
    print("Python is not installed")

#tar = tarfile.open("/tmp/tartest.tar.gz","w:gz")
for root,dirs,files in os.walk(file_path):
    tar = tarfile.open(file_dirname+dirs,"w:gz")
