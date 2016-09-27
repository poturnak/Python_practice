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
print(df.head())

# now we need to conduct exploratory data analysis on this dataset
# first we will create the scatterplot matrix that allows us to visualize the pair wise correlations
# between different features in one place
# for that purpose we will use seaborn module

import matplotlib.pyplot as plt
import seaborn as sns


sns.set(style='whitegrid', context='notebook')
cols = ['LSTAT', 'INDUS', 'NOX', 'RM', 'MEDV']

sns.pairplot(df[cols], size=2.5)
plt.tight_layout()
# plt.savefig('./figures/scatter.png', dpi=300)
plt.show()

# also to quantify the linear relationship between features we will create the correlation matrix
# correlation matrix is closely related to covariance
# in fact, correlation is the scaled version of covariance
# in facr, if you first standardize the features, then you calculate the covariance, you will get correlation
# cor(X, Y) = cov(X,Y) / (sd(x) * sd(Y)
# correlation matrix is the square matrix that contains Person product moment correlation coefficients
# these coefficients measure the linear dependance between pairs of features
# correlation is between -1 and 1
# 1 is perfect positive correlation
# 0 is no correlation
# -1 is perfect negative correlation
