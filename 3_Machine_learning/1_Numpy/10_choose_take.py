#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

# first you specify indices [n, n1, n2]
# --number of indices need to be the same as the maximum length of the array
# --all arrays are of the same length
# --indices are as high as the number of arrays to choose from
# choose takes 1st element from array n, 2nd from array n1, 3rd from array 3 etc.
# n, n1, n2 needs to be max the number of arrays

import numpy as np

choices = np.array([[0, 1, 2, 3], [10, 11, 12, 13], [20, 21, 22, 23], [30, 31, 32, 33]])
indices = [2, 3, 0, 0]

result = np.choose(indices, choices)

print(result)

# let's take a look at take example
# you also pick up the elements, but you flatten the array first
# then you pick up the element by the index
indices1 = [2, 3, 0, 1, 6]
result1 = np.take(choices, indices1)
print(result1)

# let solve the problem
# Generate a 10 x 3 array of random numbers (in range [0,1]). For each row, pick the number closest to 0.5
print('-----------')
np.random.seed(11)
arr = np.random.rand(3, 2)
print(arr)

mask = np.argmin(abs(arr - 0.5), axis=1)
print(mask)
print(arr.T)
result = np.choose(mask, arr.T)
print('\nThe result is:')
print(result)

for i in range(0, 3):
    print(arr[i][mask[i]])
