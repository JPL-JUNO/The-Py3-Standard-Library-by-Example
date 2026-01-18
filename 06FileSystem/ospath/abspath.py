"""
Created time: 2026-01-11 22:40:40
Author(s)   : Stephen CUI
File        : abspath.py
Email       : cuixuanstephen@gmail.com
Description : 从文件系统树最顶层的完整路径
"""

import os
import os.path

os.chdir("D:/The-Py3-Standard-Library-by-Example")
PATHS = [
    ".",
    "..",
    "./one/two/three",
    "../one/two/three",
]
for path in PATHS:
    print("{!r:>21} : {!r}".format(path, os.path.abspath(path)))
