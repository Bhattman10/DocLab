# ================================ PYTHON HEADER ================================= #
import os
import sys

module_dir = os.path.join(os.path.dirname(__file__), "../python")
sys.path.append(module_dir)
os.chdir("build")
del module_dir
# ================================================================================ #

import mathlib

u = (1.0, 2.0)
v = (5.0, 5.0)
dist = mathlib.distance(u, v)
print(f"The distance between {u} and {v} is {dist}.")

