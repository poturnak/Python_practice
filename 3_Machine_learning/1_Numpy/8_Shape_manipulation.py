#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

import numpy as np

# to flatten the array use the ravel function
# you can also transpose before raveling
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
b = a.ravel().copy()  # to make sure we make a copy of the array
b1 = a.T.ravel()
print(b)
print(b1)

# you can also reshape the array to the 2D form you want
print(b.shape)
b = b.reshape((3, 2))
print(b)
b[0, 0] = 99
print(a)  # if the copy was not made, you work withy reference, thus, a will also be changed

d = np.array([[1, 2, 3], [4, 5, 6]])
print(d.reshape((3, 2)))

# adding a dimension
z = np.array([1, 2, 3])
print(z[:, np.newaxis])
# you can also use [np.newaxis, :]

# dimension shuffling
v = np.arange(4*3).reshape((4, 3))
print(v)
print(v.transpose())

# you can also resize the array
m = np.arange(4)
m.resize((10, ))
print(m)

# you can also sort data
# sorting along the axis
k = np.array([[4, 3, 5], [1, 2, 1]])
k1 = np.sort(k, axis=1)
print(k1)

# sorting with fancy indexing
arr = np.array([4, 3, 1, 2])
j = np.argsort(arr)
print(j)
print(arr[j])

