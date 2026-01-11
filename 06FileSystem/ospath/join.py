"""
Created time: 2026-01-11 22:03:43
Author(s)   : Stephen CUI
File        : join.py
Email       : cuixuanstephen@gmail.com
Description :
"""

import os.path

PATHS = [
    ("one", "two", "three"),
    ("/", "one", "two", "three"),
    ("/one", "/two", "/three"),
]

for parts in PATHS:
    print("{} : {!r}".format(parts, os.path.join(*parts)))

# If any argument to join begins with os.sep, all of the previous arguments are discarded and
# the new one becomes the beginning of the return value.
