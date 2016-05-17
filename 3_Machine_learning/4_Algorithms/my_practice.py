#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

import numpy as np
import pandas as pd

df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header = None)
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)
X = df.iloc[0:100, [0, 2]].values
theta = np.array([0, 0, 0])
alpha = 0.01

ones = np.ones(100)[:, np.newaxis]

X = np.hstack((ones, X))

for i in range(1):
    net_input = np.dot(X, theta)
    error = net_input - y
    theta = theta - alpha * (np.dot(X.T, error))

print(theta)


m = np.array([[1, 2, 3], [4, 5, 6]])
print(m[0,1])