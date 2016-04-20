#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
import numpy as np

a = np.array([[1, 2], [3, 4], [4, 5]])
b = [1, 2, 3]

c = np.dot(a, b)
print(a)
print(c)