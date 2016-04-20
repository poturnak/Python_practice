#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap


class Perceptron():
    """Perceptron classifier
        eta: learning rate (between 0.0 and 1.0), float type
        n_iter: number of epochs, int
        w_: 1D-array, weights after training
        errors_: list, number of mis-classifications in every epoch """
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    def predict(self, X):
        """ Return class label after unit step"""
        return np.where(self.net_input(X) >= 0, 1, -1)

    def net_input(self, X):
        """ Calculate net input"""
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def fit(self, X, y):
        """Training perceptron
            X: array of training vectors, shape = [n_samples, n_features]
            y: vector of correct predictions, shape = [n_samples] """
        self.w_ = np.zeros(1 + X.shape[1])  # need +1 weight since w0, all weights are 0 initially
        self.errors_ = []

        for _ in range(self.n_iter):  # here we determine the iterations based on epochs
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

# ---------------------------------------------------------------------------------------------------


def plot_decision_regions(X, y, classifier, resolution=0.02):
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha = 0.4, cmap = cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # plot class samples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(X[y == cl, 0], X[y == cl, 1], alpha=0.8, c = cmap(idx), marker=markers[idx], label=cl)

# ---------------------------------------------------------------------------------------------------
# let's use pandas to import the dataset
df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header = None)
# print(df.tail())

# next we need to extract first 100 labels that correspond to setosa and versicolor (only 2 types)
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)

# not let's build the X array and extract the 100 first features (sepal length and petal length) and put that into array
X = df.iloc[0:100, [0, 2]].values

# not let's visualize the features that we extracted
plt.scatter(X[:50, 0], X[0:50, 1], c='red', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolor')
plt.xlabel('petal length [cm]')
plt.ylabel('sepal length [cm]')
plt.legend(loc='upper left')
plt.show()

# now let's train our perceptron with the data that we just extracted
ppn = Perceptron(eta=0.1, n_iter=100)
ppn.fit(X, y)
plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of misclassifications')
plt.show()

# let's plot the contour plot
plot_decision_regions(X, y, classifier=ppn)
plt.xlabel('sepal length [cm]')
plt.ylabel(' petal length [cm]')
plt.legend( loc ='upper left')
plt.show()

print('Calculated weights are: ', ppn.w_)
