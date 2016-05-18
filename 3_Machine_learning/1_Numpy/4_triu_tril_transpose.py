#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
print(arr)

b = np.triu(arr, k=1)  # k=1 takes 1 element in the first row and draws diagonal from it, triu returns the upper part
# tril returns the lower part
print(b)

print(b.transpose())  # transposes the array, line becomes a column, then next line, etc.
# you can transpose only 2D array; 1D array will not be changed

a = np.arange(0, 10)
print(a)
print(a.transpose())  # not changed

# for that purpose you need to use newaxis
print(a[:, np.newaxis])
print(a)