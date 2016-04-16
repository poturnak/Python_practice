#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

import numpy as np
from matplotlib import pyplot as plt

n_stories = 10
t_max = 20

t = np.arange(t_max)
steps = 2 * np.random.random_integers(0, 1, (n_stories, t_max)) - 1

positions = np.cumsum(steps, axis=1)
sq_distance = positions**2

mean_sq_distance = np.mean(sq_distance, axis=0)
print(mean_sq_distance)

# plotting the results
plt.plot(t, np.sqrt(mean_sq_distance), 'g.', t, np.sqrt(t), 'y-')
plt.show()

