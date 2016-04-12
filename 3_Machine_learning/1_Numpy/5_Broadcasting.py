#! /library/Frameworks/Python.frameork/Versions/3.5/python3.5w
# when we add/subtract the arrays of different shape, numpy needs to do the broadcasting
# broadcasting is when you bring arrays to the same dimensions

import numpy as np

arr = np.tile(np.arange(0, 40, 10), (3, 1))
arr = arr.transpose()
print(arr)

# arr1 = np.array([0, 1, 2])
# print(arr1)
#
# print(arr + arr1)
#
# another form of broadcasting
# a = np.arange(0, 40, 10)
# a = a[:, np.newaxis]
# print(a)
#
# print(a + arr1)

# let's work on the example

mileposts = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
distance = np.abs(mileposts - mileposts[:, np.newaxis])
print(distance)

x, y = np.arange(5), np.arange(5)[:, np.newaxis]
distance = np.sqrt(x ** 2 + y ** 2)
print(distance)
