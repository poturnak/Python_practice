#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

import numpy as np

# meshgrid creates the mesh of all coordinates
# take vector x and vector y
# generate all coordinates from that vector
# x1,y1, x2y2, etc.

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
z = np.meshgrid(x, y)

print(z[0])
print(z[1])
