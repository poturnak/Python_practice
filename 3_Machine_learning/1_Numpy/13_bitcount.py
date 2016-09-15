#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

import numpy as np

# np.bincount counts the number of value occurrences in the numpy array
# when the results are returned the array will be sorted by the values of the original array
# in the results below 0 comes first with 0 occurences

a = np.array([3, 3, 0, 0, 0, 1, 2])
print(np.bincount(a))

# we can also assign weigths to the each element of the array
# therefore, bincount will return the sum of weights for each value
# again, the results will be sorted by the values int he original array

a = np.array([3, 3, 0, 0, 0, 1, 2])
weights = [0.2, 0.1, 0.4, 0.5, 0.9, 0.1, 0.1]
print(np.bincount(a, weights=weights))

# we can emulate this fucntionality using the following code

a = np.array([3, 0, 1, 2])
w = np.array([0.2, 0.8, 0.6, 0.3])
u = np.unique(a)
calc = np.zeros((len(a)))

for i, j in zip(a, w):
    calc[np.where(u == i)[0][0]] += j
print(calc.argmax())

