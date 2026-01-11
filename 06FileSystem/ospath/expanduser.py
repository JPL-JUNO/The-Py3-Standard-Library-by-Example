"""
Created time: 2026-01-11 22:13:37
Author(s)   : Stephen CUI
File        : expanduser.py
Email       : cuixuanstephen@gmail.com
Description :
"""

import os.path

for user in ["", "dhellmann", "nosuchuser"]:
    lookup = "~" + user
    print("{!r:>15} : {!r}".format(lookup, os.path.expanduser(lookup)))

# 还可以处理包含可变部分的路径，这些可变部分可以自动拓展
# 如果用户的主目录无法找到，那么字符串将不会做任何改动并直接返回
