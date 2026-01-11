"""
Created time: 2026-01-11 22:29:37
Author(s)   : Stephen CUI
File        : normpath.py
Email       : cuixuanstephen@gmail.com
Description :
"""

import os.path

PATHS = [
    "one//two//three",
    "one/./two/./three",
    "one/../alt/two/three",  # 不是 .. 的情况下，放到栈中，遇到 .. 再 pop
]

for path in PATHS:
    print("{!r:>22} : {!r}".format(path, os.path.normpath(path)))

# 使用 join() 或利用嵌入变量由单独的字符串组合路径时，
# 得到的路径最后可能会有多余的分隔符或相对路径部分
