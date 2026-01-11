"""
Created time: 2026-01-11 21:55:36
Author(s)   : Stephen CUI
File        : splitext.py
Email       : cuixuanstephen@gmail.com
Description :
"""

import os.path

PATHS = [
    "filename.txt",
    "filename",
    "/path/to/filename.txt",
    "/",
    "",
    "my-archive.tar.gz",  # 只是用 os.extsep 的最后一次出现
    "no-extension.",
]

for path in PATHS:
    print("{!r:>23} : {!r}".format(path, os.path.splitext(path)))

# Only the last occurrence of os.extsep is used when looking for the extension.
# Thus, if a filename has multiple extensions,
# the results of splitting it leaves part of the extension on the prefix.
