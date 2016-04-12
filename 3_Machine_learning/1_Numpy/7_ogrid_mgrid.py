#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

# ogrid allows to create 2 vectors that you can then broadcast and do operations on them
# typically you can do that manually with [:, np.newaxis]

import numpy as np

a = np.ogrid[0:5, 0:5]
print(a[0])
print(a[1])

c = a[0] + a[1]
print(c)

# mgrid will provide generated matrices right away

a, b = np.mgrid[0:4, 0:4]
print(a)
print(b)

