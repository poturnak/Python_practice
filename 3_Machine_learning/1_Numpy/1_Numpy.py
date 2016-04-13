#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# ============================================================================================
# _________________ Intro _________________
# var.ndim - show number of dimensions (rows)
# var.shape - show the number of items in the dimension
# var.dtype - print the data type of the elements in the array
# --floats are displayed with the trailing comma
# --you can explicitly specify the data type that you want by passing dtype when creating array
# dtypes = float, bool, S7, etc.
# [:, np.newaxis] - adds a new axis when printing an array

# _________________ Creating numpy array _________________
# arr = numpy.array([a, b, c, ..]) - create numpy array
# arr = np.arange(10) - create one dimensional array from 0 to 9
# arr = np.arange(start, end, step) - create array using beginning, end and step
# arr = np.linspace(start, end, numpoints) - create array using number of steps between the endpoints
# arr = np.linspace(0, 1, 5) - 0 to 1 creating 5 numpoints
# np.ones((n, n, n)) - crate 1, 2, 3 dimensional array consisting of ones
# np.zeroes((n, n, n)) - create the 1, 2, 3, dimensional array of zeroes
# np.eye() - returns 2D array with 1s in the diagonal and 0s elsewhere
# np.diag(np.array([1, 2, 3]) - array with 1, 2, 3 in the diagonal
# np.empty((n, n, n)) - return array of given shape without initializing values

# _________________ Random number generation _________________
# np.random.seed(value) - set the initial value for pseudo random number generation algorithm
# np.random.rand(x, y) - generate array of random numbers with x rows and y columns; number from [0, 1]
# np.random.randint(low, high=None, size=None) - return random integers from [low, high)
# np.random.random_integers(low, high=None, size=None) - return random integers from low(inclusive) to high(inclusive)

# _________________ Indexing and slicing _________________
# --you can do just indexing to extract data or you can assign values using indexing
# --SINGLE ELEMENT INDEXING
# arr[n, n, n] - get the item from the array; indices begin at 0; returns a single item
# --you can get the whole line if you omit some indexes
# arr[n] - returns the whole line if arr is multidimensional array
# --SLICING FOR INDEXING
# --slicing returns the view of the array
# arr[::-1] - reversing the array
# --when indexing 1. row (x), 2. column(y), 3. variable(z)
# --when slicing 1. Start 2. Stop 3. Step
# var[2:6:2] - start from item 2 till 5 with the step 2, you will get the slice
# var[::2] - going through all array, get every second item
# var[0, 3:5] - look at 2D array, get 1st line and extract slice from 3:5
# var[2::2, ::2] - start at row 2, go till the end and choose every second row
#                - then within those rows, choose every second item from the beginning
# --you can also combine assignment and slicing
# var[5:] = 10 - starting from item 5 assign 10 to each item till the end
# --USING ARRAYS FOR INDEXING
# --using arrays for indexing will return the new array
# arr[[1, 5, 6, 7]] - create new array with elements indexes you want to extract
#                           - then using arr return those elements
# arr[[0, 1], [1, 2]] - in this case your elements will be [0,1], and [1, 2]
# --FANCY INDEXING WITH MASKS OR BOOLEAN ARRAYS
# --create a mask
# mask = (arr > 20)
# --then index using this mask
# arr[mask] - will get all the elements that are more than 20
# --you can use assignment usign mask as well
# arr[mask] = value
# _________________ Tiling an array _________________
# numpy.tile(A, reps) - construct the array repeating A the reps times
# np.tile(b, (2, 1)) - repeat b 2 times, do 1 row
# _________________ Copies and views _________________
# --slicing creates a view of the array, thus 2 arrays share the same memory space
# --to create a slice in a new memory location you need to force copy
# a = b[::2].copy() - forcing a copy on a slice
# _________________ Numerical operations on arrays _________________
# --to add to each element in array just ad the mumber
# arr + 1 - will add 1 to each element
# --to multiply, subtract, divide apply those operations on array
# --you can do comparisons of each element between 2 arrays
# a == b, a > b - each element of a is compared with element b and the bitvector is generated
# np.array_equal(a, b) - array wise comparisons (will retunrn only True or False)
# np.logical_or(a, b) - do logical or with each element a with element b
# np.logical_and(a, b) - do logical and between elements
# np.sin(a), np.log(a), np.exp(a) - do operations on each element of a
# np.sum(arr) - calculates the sum of all the elements
# np.sum(axis=0) - returns the sum of all elements in each column (a, b, c) for matrix of 3 columns
# np.sum(axis=1) - returns the sum of all elements in each row
# --you can return the sum of each specific column or row
# arr[0, :].sum() - return the sum of elements in row 0
# arr.min(), arr.max() - get min or max element
# arr.argmin(), arr.argmax() - get index of min or max element
# arr.mean(axis optional) - return mean
# arr.median(axis optional) - return median
# arr.std(axis optional) - return std
# np.unique(arr) - find unique elements of the array
# --axis=0 - over the column, axis=1 - over the row
# _________________ Data types operations _________________
# np.round(arr) - round all floats to significant integer; still be float
# np.astype(int) - only retrive integers from float and represent array with integers
# np.round(arr).astray(int) - round arr first then extract integers
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

# generate some random numbers
np.random.seed(10)
f = np.random.rand(5, 5)
print(f)

# Let's practice some mask indexing here
arr = np.random.random_integers(0, 20, 15)
print(arr)
mask = (arr > 10)
print(mask)
print(arr[mask])

b = np.array([[1, 2, 3, 4, 5],
              [0, 1, 2, 3, 4]])
print(b)

print(b[np.array([1, 1]), [3, 4]])

print(np.random.random_integers(0, 1, (10, 5)))
