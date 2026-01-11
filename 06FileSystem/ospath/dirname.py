"""
Created time: 2026-01-11 21:47:17
Author(s)   : Stephen CUI
File        : dirname.py
Email       : cuixuanstephen@gmail.com
Description :
"""

import os.path

PATHS = [
    "/one/two/three",
    "/one/two/three/",
    "/",
    ".",
    "",
]

for path in PATHS:
    print("{!r:>17} : {!r}".format(path, os.path.dirname(path)))

# dirname 函数返回分解路径得到的第一部分
