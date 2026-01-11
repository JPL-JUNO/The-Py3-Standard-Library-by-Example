"""
Created time: 2026-01-11 22:01:17
Author(s)   : Stephen CUI
File        : commonpath.py
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
print("PREFIX:", os.path.commonpath(paths))

# commonpath() does honor path separators.
# It returns a prefix that does not include partial path values.
