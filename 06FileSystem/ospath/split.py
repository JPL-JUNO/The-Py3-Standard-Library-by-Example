"""
Created time: 2026-01-11 14:53:37
Author(s)   : Stephen CUI
File        : split.py
Email       : cuixuanstephen@gmail.com
Description :
"""

import os.path

PATHS = [
    "./one/two/three",
    "/one/two/three/",
    "/",  # 参数以 os.sep 结尾时，路径的最后一个元素是一个空字符串
    ".",
    "",
]

for path in PATHS:
    print("{!r:>17}: {}".format(path, os.path.split(path)))
