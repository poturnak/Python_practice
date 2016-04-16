#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

from matplotlib import pyplot as plt
import numpy as np

# Building a simple plot
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
c, s = np.cos(x), np.sin(x)

# generating default plotting:
# plt.plot(x, c)
# plt.plot(x, s)
# plt.show()

# to customize the plotting parameters we use the following
# create a figure size with the dpi
plt.figure(figsize=(5, 5), dpi=80)

# create a new subplot from figure
plt.subplot(2, 1, 1)  # you can plot multiple charts on one chart area
# you specify (# rows, # of columns, plot reference)
# then you plt the chart
# then specify subplot with other reference and plot other chart

# you can also assign names to axes
plt.xlabel('Numbers')
plt.ylabel('Values')

# you can place random text on the chart
plt.text(-2, 0, r'$\mu=100,\ \sigma=15$')

# Plot cosine with a blue continuous line of width 1 (pixels)
plt.plot(x, c, color="blue", linewidth=1.0, linestyle="-", label='cosine')

# Plot sine with a green continuous line of width 1 (pixels)
plt.plot(x, s, color="green", linewidth=1.0, linestyle="-", label='sine')

# Set x limits
plt.xlim(-4.0, 4.0)

# Set x ticks
plt.xticks(np.linspace(-4, 4, 5, endpoint=True))  # (beg, end, # of ticks)
# you can also just pass an array to xticks()


# Set y limits
plt.ylim(-1.0, 1.0)

# Set y ticks
plt.yticks([-1, 0, 1])

# we can also add the legend
# you first need to specify label in the plot() function
plt.legend(loc='lower right')

plt.subplot(2, 1, 2)
Z = np.random.uniform(0, 1, 20)
plt.pie(Z)

plt.show()
plt.close(1)

plt.figure(figsize=(5, 5), dpi=80)
Z = np.random.uniform(0, 1, 20)
plt.pie(Z)
plt.show()


