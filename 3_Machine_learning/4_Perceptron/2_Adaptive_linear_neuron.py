#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# Adaline is an improvement over the initial perceptron introduced by Rosenbalt
# here the weights are updated based on linear activation function but not the step function

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


class AdalineGD( object):
    """ ADALINE.
        eta : float, learning rate (between 0.0 and 1.0)
        n_iter : number of epochs."""
    def __init__(self, eta = 0.01, n_iter = 50):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        """ Train ADALINE
            X : {array-like}, shape = [n_samples, n_features] Training vectors
            y : array-like, shape = [n_samples] Target values"""
        self.w_ = np.zeros(1 + X.shape[1])
        self.cost_ = []
        for i in range(self.n_iter):
            output = self.net_input(X)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors ** 2).sum() / 2.0
            self.cost_.append(cost)
        return self

    def net_input(self, X):
        """ Calculate net input"""
        return np.dot(X, self.w_[1:]) + self.w_[ 0]

    def activation( self, X):
        """ Compute linear activation"""
        return self.net_input( X)

    def predict( self, X):
        """ Return class label after unit step"""
        return np.where(self.activation(X) >= 0.0, 1, -1)
# ______________________________________________________________________________________________________

# let's use pandas to import the dataset
df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header = None)
# print(df.tail())

# next we need to extract first 100 labels that correspond to setosa and versicolor (only 2 types)
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)

# not let's build the X array and extract the 100 first features (sepal length and petal length) and put that into array
X = df.iloc[0:100, [0, 2]].values

# now let's train our ADALINE with the data that we just extracted
ppn = AdalineGD(eta=0.1, n_iter=100)
ppn.fit(X, y)


