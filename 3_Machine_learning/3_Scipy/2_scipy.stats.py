#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

# probability density function
a = np.random.normal(size=1000)
print(a)
bins = np.arange(-4, 5)
print(bins)

# compute the histogram, returns probability density of the values in each bin
histogram = np.histogram(a, bins=bins, density=True)[0]
print(histogram)

bins = 0.5 * (bins[1:] + bins[:-1])
print(bins)

b = stats.norm.pdf(bins)

plt.plot(bins, histogram)
plt.plot(bins, b)
plt.show()
