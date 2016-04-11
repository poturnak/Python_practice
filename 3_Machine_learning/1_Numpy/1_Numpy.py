#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# ============================================================================================
# var = numpy.array([]) - create numpy array
# print(np.lookfor('create array')) - generate the list of potential functions for the question
# var.ndim - show number of dimensions (rows)
# var.shape - show the number of items in the dimension
# var = np.arange(10) - create one dimensional array from 0 to 9
# var = np.arange(start, end, step) - create array using beginning, end and step
# var = np.linspace(start, end, numpoints) - create array using number of steps between the endpoints
# var.dtype - print the data type of the elements in the array
# --floats are displayed with the trailing comma
# --you can explicitly specify the data type that you want by passing dtype when creating array
# dtypes = float, bool, S7, etc.
# var = np.linspace(0, 1, 5)
# [:, np.newaxis] - adds a new axis when printing an array
# _________________ Creating common arrays _________________
# np.ones((n, n, n)) - crate 1, 2, 3 dimensional array consisting of ones
# np.zeroes((n, n, n)) - create the 1, 2, 3, dimensional array of zeroes
# np.eye() - returns 2D array with 1s in the diagonal and 0s elsewhere
# np.diag(np.array([1, 2, 3]) - array with 1, 2, 3 in the diagonal
# np.random.rand(4) - 1D array with 4 random numbers
# np.empty((n, n, n)) - return array of given shape without initializing values
# _________________ Indexing and slicing _________________
# var[n, n, n] - get the item of the list; indices begin at 0
# var[::-1] - reversing the array
# --when indexing 1. row (x), 2. column(y), 3. variable(z)
# --when slicing 1. Start 2. Stop 3. Step
# var[2:6:2] - start from item 2 till 5 with the step 2, you will get the slice
# var[::2] - going through all array, get every second item
# var[0, 3:5] - look at 2D array, get 1st line and extract slice from 3:5
# var[2::2, ::2] - start at row 2, go till the end and choose every second row
#                - then within those rows, choose every second item from the beginning
# --you can also combine assignment and slicing
# var[5:] = 10 - starting from item 5 assign 10 to each item till the end
# _________________ Tiling an array _________________
# numpy.tile(A, reps) - construct the array repeating A the reps times
# np.tile(b, (2, 1)) - repeat b 2 times, do 1 row
# _________________ Copies and views _________________
# --slicing creates a view of the array, thus 2 arrays share the same memory space
# --to create a slice in a new memory location you need to force copy
# a = b[::2].copy() - forcing a copy on a slice
# ============================================================================================

import numpy as np

# let's create the array
a = np.array([0, 1, 2, 3, 4])
print(a.ndim)
print(a.shape)

b = np.array([[1, 2, 3, 4, 5],
              [0, 1, 2, 3, 4]])
print(b.ndim)
print(b.shape)

c = np.array([[[1, 2, 3], [4, 5, 6]], [[6, 7, 8], [9, 10, 11]], [[12, 13, 14], [15, 16, 17]]])
print(c.shape)

a = np.arange(10)
print(a)

a = np.arange(1, 9, 3)
print(a)

c = np.linspace(0, .5, 4)

# creating common arrays
a = np.ones((5, 5, 5))
print(a)

a = np.random.rand(3, 3, 3)
print('Random array ')
print(a)

d = np.empty([2, 2, 3])
print(d)

print(d[0][0][2])  # indexing starts with '0'!!!
print(d[0, 0, 2])

print('\n\n')
array = np.arange(6) + np.arange(0, 51, 10)[:, np.newaxis]
print(array)

b = np.array([[4, 3], [2, 1]])
print(np.tile(b, (2, 2)))

print('\n')
a = np.diag([2, 3, 4, 5, 6])
print(a)
