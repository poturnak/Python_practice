#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

from scipy import io as spio
from scipy import misc
# matplotlib also has similar fucntion plt.imread
import numpy as np

# with this module you can save and load matlab files

a = np.ones((3, 3))
spio.savemat('file.mat', {'a': a})  # it expects the dictionary and lets you store variables

# let's load this file
data = spio.loadmat('file.mat')
print(data['a'])

misc.imread('fname.png')
