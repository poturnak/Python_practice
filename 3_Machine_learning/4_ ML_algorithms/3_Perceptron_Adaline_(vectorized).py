#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# This difference for Adaline that we use net-input values to undate the weights
# Once you get net input, you subtract the target value and then adjust weights
# For perceptron you convert predicted value to step function first, then you update weights

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.colors import ListedColormap


class Perceptron:
    """Basic perceptron classifier with gradient decent (vectorized implementation)
        eta - learning rate
        n_iter - number of epochs
        theta - weights after training
    """
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter
        self.theta = np.array([[0.], [0.], [0.]])  # instead of all zeroes you can initialize weights randomly
        self.cost = []
        self.error = []

    def fit(self, X, y):
        X = np.hstack((np.ones((X.shape[0], 1)), X))  # we add column of ones to account for bias
        # self.theta = np.random.rand(X.shape[1], 1)  # theta is a column vector
        for _ in range(self.n_iter):
            self.theta -= np.dot(X.T, (np.dot(X, self.theta) - y[:, np.newaxis])) / X.shape[0]* self.eta
            self.calculate_cost(X)

    def calculate_cost(self, X):
        errors = self.predict(X) - y[:, np.newaxis]
        self.error.append(np.count_nonzero(errors))
        self.cost.append(np.sum(((np.dot(X, self.theta) - y[:, np.newaxis])** 2) / X.shape[0] / 2))

    def predict(self, X, flag=False):
        if flag:
            X = np.hstack((np.ones((X.shape[0], 1)), X))
        return np.where(np.dot(X, self.theta) > 0, 1, -1)


def plot_decision_regions(X, y, classifier, resolution=0.02):
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T, flag=True)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # also we will plot the the samples on the same contour chart
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(X[y == cl, 0], X[y == cl, 1], alpha=0.9, c=cmap(idx), marker=markers[idx], label=cl)
# ---------------------------------------------------------------------------------------------------
# let's use pandas to import the dataset
df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)

# next we need to extract first 100 labels that correspond to setosa and versicolor (only 2 types)
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)
X = df.iloc[0:100, [0, 2]].values

# now let's visualize the features that we extracted
plt.scatter(X[:50, 0], X[0:50, 1], c='red', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolor')
plt.xlabel('petal length [cm]')
plt.ylabel('sepal length [cm]')
plt.legend(loc='upper left')
plt.show()
# ---------------------------------------------------------------------------------------------------
# now let's train our perceptron with the data that we just extracted
ppn = Perceptron(eta=0.01, n_iter=100)
ppn.fit(X, y)

# now let's plot the cost function & number of misclassifications for our perceptron
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(range(len(ppn.cost)), ppn.cost, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Cost function')
plt.subplot(2, 1, 2)
plt.plot(range(len(ppn.error)), ppn.error, marker='x', color='red')
plt.xlabel('Epochs')
plt.ylabel('Error misclassification')
plt.show()

# let's plot the contour plot
plot_decision_regions(X, y, classifier=ppn)
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')
plt.show()

print(ppn.theta)
print(ppn.error)
print(ppn.cost)
