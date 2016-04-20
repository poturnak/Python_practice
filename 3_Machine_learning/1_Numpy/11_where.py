#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

import numpy as np

# where lets; you specify condition (mask)
# then you can choose elements from x if true, otherwise elements from y will be returned

# in this particular case we are working with 2D array
# it returns the index array
# elements that  are more that 5 will be 2,0, 2,1, 2,2
x = np.arange(9.).reshape(3, 3)
print(x)
print(np.where(x > 5))

# in this particular scenario we will specify x and y
# x is what ti return in case true, y is what to return in case false

print(np.where(x>5, 1, 2))

b = np.arange(10)
