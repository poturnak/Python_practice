#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

import numpy as np

a = np.exp(2j*np.pi*np.arange(3))
print(a)
print(a[:,np.newaxis])
print(a[np.newaxis, :])
b = a[:,np.newaxis] + a[np.newaxis,:]
np.fft.fftn(b)



arr = np.arange(35).reshape(5, 7)
print(arr)

print(arr[[1, 3, 3]])
print(arr.shape)


array = np.arange(6) + np.arange(0, 51, 10)[:, np.newaxis]
print(array)