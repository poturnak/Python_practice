#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

# tile repeats the array certain number of times
# (a, b) - a is numbers of rows, b is number of columns

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
b = np.tile(arr, (2, 1))
print(b)

arr1 = np.array([[1, 2], [3, 4]])
c = np.tile(arr1, (2,1))
print(c)