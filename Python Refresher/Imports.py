# 1️⃣ Why imports are used
#
# import lets you reuse code written in:
# 
# Python standard libraries
#
# Third-party packages
#
# Your own files (modules)
#
# Instead of rewriting logic, you import and use it.
#
# 2️⃣ Basic import
# import math
# print(math.sqrt(16))
#
#
# ✔ Imports the entire module
# ✔ Access using module_name.function
#
# 3️⃣ Import with alias (as)
# import numpy as np
#
#
# ✔ Shortens long names
# ✔ Very common in real projects
#
# 4️⃣ Import specific items
# from math import sqrt, pi
# print(sqrt(25))
#
#
# ✔ No need to write math.
# ⚠ Only imports what you specify
#
# 5️⃣ Import everything (NOT recommended)
# from math import *
#
#
# ❌ Bad practice
# ❌ Can overwrite variable names
# ✔ Sometimes seen in small scripts
#
# 6️⃣ Import your own Python file (module)
#
# Assume file: utils.py
#
# # utils.py
# def add(a, b):
#     return a + b
#
# import utils
# print(utils.add(2, 3))
#
#
# OR
#
# from utils import add
# print(add(2, 3))
#
# 7️⃣ Common standard library imports (must know)
# import math        # maths
# import random      # random numbers
# import datetime    # date & time
# import sys         # system-level access
# import os          # files & directories
#
# 8️⃣ Import order (good practice)
# # 1. Standard library
# import os
# import sys
#
# # 2. Third-party
# import numpy as np
#
# # 3. Local files
# import utils
#
# 9️⃣ Check what a module contains
# import math
# print(dir(math))
#
# 1️⃣0️⃣ Key exam / interview points
#
# ✔ Import happens only once
# ✔ Modules improve code reusability
# ✔ as improves readability
# ✔ Avoid import *
# ✔ Python searches modules via sys.path