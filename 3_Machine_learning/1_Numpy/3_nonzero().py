#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

# nonzero() returns the tuple of arrays
# for 1 dimensional array there will be one item, for 2D 2 items, for 3D 3 items
# then each tuple represent the index value
# 1st tuple is row of non zeor item, 2nd tuple is column etc.

import numpy as np

a = np.diag([1, 2, 3, 4, 5])
print(a)

b = a.nonzero()
print(b)

print(a[a.nonzero()])  # returns all nonzero items from the array
