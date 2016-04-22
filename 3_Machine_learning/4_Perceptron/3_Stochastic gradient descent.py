#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

# Stochastic descent is sometimes referred to as interactive or online gradient descent
# Instead of updating weights after the whole run on the dataset, we can be updating weight incrementally
# Meaning for each training sample
# Even though it is approximation of gradient, it reaches convergence faster due to more frequent weight updates
# For stochastic gradient descent we need to shuffle the date before each epoch
# We also can replace fixed learning rate with dynamically decreasing learning rate over time
# learning rate = c / (number_of_iterations + c1) - where c and c1 are constants
# Stochastic gradient descent also allows online learning, meaning when new data arrives we will adjust on the fly
# Sometimes it is beneficial to use mini-batch learning type
# That is the middle between batch learning and stochastic gradient descent
# Allows us to converge faster, calculate better gradient, and also perform vectorized operations
# as opposed to going through for loop and analyzing each training sample

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.colors import ListedColormap
from numpy.random import seed


class AdalineSGD( object):
    """ ADALINE with stochastic gradient descent"""

    def __init__(self, eta=0.01, n_iter=10, shuffle=True, random_state=None):
        self.eta = eta
        self.n_iter = n_iter
        self.w_initialized = False
        self.shuffle = shuffle
        if random_state:
            seed(random_state)

    def _initialize_weights(self, m):
        """ Initialize weights to zeros"""
        self.w_ = np.zeros(1 + m)
        self.w_initialized = True

    def _shuffle(self, X, y):
        """ Shuffle training data"""
        r = np.random.permutation(len(y))
        return X[r], y[r]

    def net_input(self, X):
        """ Calculate net input"""
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def activation(self, X):
        """ Compute linear activation"""
        return self.net_input(X)

    def predict(self, X, y):
        return np.where(self.activation(X) >= 0.0, 1, -1)

    def _update_weights(self, xi, target):
        """ Apply Adaline learning rule to update the weights"""
        output = self.net_input(xi)
        error = (target - output)
        self.w_[1:] += self.eta * xi.dot(error)
        self.w_[0] += self.eta * error
        cost = 0.5 * error ** 2
        return cost

    def fit(self, X, y):
        self._initialize_weights(X.shape[1])
        self.cost_ = []
        for i in range(self.n_iter):
            if self.shuffle:
                X, y = self._shuffle(X, y)
            cost = []
            for xi, target in zip(X, y):
                cost.append(self._update_weights(xi, target))
                avg_cost = sum(cost) / len(y)
                self.cost_.append(avg_cost)
        return self

    def partial_fit(self, X, y):
        if not self.w_initialized:
            self._initialize_weights(X.shape[1])
        if y.ravel().shape[0] > 1:
            for xi, target in zip(X, y):
                self._update_weights(xi, target)
        else: self._update_weights(X, y)
        return self

# ___________________________________________________________________________________________________
