#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

# Regression analysis is used to predict the variables on a continuous scale
# The goal of a simple linear regaression model is to model the relationship
# between signle feature (explanatory variable x) and a continuous valued response y.
#  y = w0 + w1*x

# regression is different from pca in a way that pca minimizes the projection errors (perpendicular
# projection from endpoints onto the pca component)
# the regression is minimizing offsets - errors of prediction

import pandas as pd

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/'
                 'housing/housing.data',
                 header=None,
                 sep='\s+')

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS',
              'NOX', 'RM', 'AGE', 'DIS', 'RAD',
              'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
df.head()