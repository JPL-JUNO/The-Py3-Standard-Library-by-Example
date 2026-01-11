"""
Created time: 2026-01-11 21:33:14
Author(s)   : Stephen CUI
File        : basename.py
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
    print("{!r:>17} : {!r}".format(path, os.path.basename(path)))
# 整个路径会剥除到只剩下一个元素，不论这指示的是一个文件还是一个目录
# 如果路径以目录分隔符结尾，则认为 base 部分为空
