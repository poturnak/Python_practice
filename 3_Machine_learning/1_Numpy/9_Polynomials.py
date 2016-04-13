#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

import numpy as np

p = np.poly1d([3, 2, -1])
print(p.roots)


m = np.arange(1, 16).reshape((3, 5)).T
print(m)

k = m[2:5:2, ::]
print(k)

a = np.arange(25). reshape((5, 5))
print(a)

b = np.array([1., 5, 10, 15, 20])

c = a / b[:, np.newaxis]
print(c)
