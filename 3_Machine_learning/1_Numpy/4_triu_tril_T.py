#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
print(arr)

b = np.triu(arr, k=1)  # k=1 takes 1 element int he first row and draws diaginal from it, triu returns the upper part
# tril returns the lower part
print(b)

print(b.T)  # transposes the array, line becomes a colum, then next line, etc.
