"""
Created time: 2026-01-11 21:58:37
Author(s)   : Stephen CUI
File        : commonprefix.py
Email       : cuixuanstephen@gmail.com
Description :
"""

import os.path

paths = [
    "/one/two/three/four",
    "/one/two/threefold",
    "/one/two/three/",
]
for path in paths:
    print("PATH:", path)
print()

print("PREFIX:", os.path.commonprefix(paths))

# 返回一个字符串，表示所有路径中都出现的公共前缀，（本质就是字符串的交集）
# 返回的字符串可能根本不是有效的路径
