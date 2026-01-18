"""
Created time: 2026-01-18 16:53:45
Author(s)   : Stephen CUI
File        : properties.py
Email       : cuixuanstephen@gmail.com
Description : 文件时间
"""

import os.path
import time

print("File         :", __file__)
print("Access time  :", time.ctime(os.path.getatime(__file__)))  # access time
print("Modified time:", time.ctime(os.path.getmtime(__file__)))  # modification time
print("Change time  :", time.ctime(os.path.getctime(__file__)))  # creation time
print("Size         :", os.path.getsize(__file__))  # 字节数
