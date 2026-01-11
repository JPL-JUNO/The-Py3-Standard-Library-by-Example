"""
Created time: 2026-01-11 22:26:48
Author(s)   : Stephen CUI
File        : expandvars.py
Email       : cuixuanstephen@gmail.com
Description : expandvars()
"""

import os.path
import os

os.environ["MYVAR"] = "VALUE"

print(os.path.expandvars("/path/to/$MYVAR"))

# expandvars() is more general,
# and expands any shell environment variables present in the path.
