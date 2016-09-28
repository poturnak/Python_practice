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
# these coefficients measure the linear dependence between pairs of features
# correlation is between -1 and 1
# 1 is perfect positive correlation
# 0 is no correlation
# -1 is perfect negative correlation

import numpy as np

# for corrvar it is required that each variable is a row with column being the value
# when passing the data you can eiother transpose the data or use the rowvar=0
# rowvar=0 means each column is a variable
# rowvar=1 (default) means each row is the variable
cm = np.corrcoef(df[cols].values, rowvar=0)
sns.set(font_scale=1.5)
hm = sns.heatmap(cm,
                 cbar=True,
                 annot=True,
                 square=True,
                 fmt='.2f',
                 annot_kws={'size': 15},
                 yticklabels=cols,
                 xticklabels=cols)

# plt.tight_layout()
# plt.savefig('./figures/corr_mat.png', dpi=300)
plt.show()

# ------------------------------------------------------------------------------------------------------
# in the part we will look at the OLS (Ordinary Least Squares) method to fit the line through the data
# This method minimizes the sum of the squared vertical distances to the sample points
# the cost function that we will try to minimize is the following
# J(w) = 1/2 * sum(1,n) (yi - yipred)^2

class LinearRegressionGD(object):

    def __init__(self, eta=0.001, n_iter=20):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.cost_ = []

        for i in range(self.n_iter):
            output = self.net_input(X)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost_.append(cost)
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return self.net_input(X)

X = df[['RM']].values
y = df['MEDV'].values

from sklearn.preprocessing import StandardScaler


sc_x = StandardScaler()
sc_y = StandardScaler()
X_std = sc_x.fit_transform(X)
y_std = sc_y.fit_transform(y)

lr = LinearRegressionGD()
lr.fit(X_std, y_std)

plt.plot(range(1, lr.n_iter+1), lr.cost_)
plt.ylabel('SSE')
plt.xlabel('Epoch')
plt.tight_layout()
# plt.savefig('./figures/cost.png', dpi=300)
plt.show()

# next let's see how well the regression fits the line

def lin_regplot(X, y, model):
    plt.scatter(X, y, c='lightblue')
    plt.plot(X, model.predict(X), color='red', linewidth=2)
    return

lin_regplot(X_std, y_std, lr)
plt.xlabel('Average number of rooms [RM] (standardized)')
plt.ylabel('Price in $1000\'s [MEDV] (standardized)')
plt.tight_layout()
# plt.savefig('./figures/gradient_fit.png', dpi=300)
plt.show()

# to scale the variable back using standard scaler we can use inverse_transform method
num_rooms_std = sc_x.transform([5.0])
price_std = lr.predict(num_rooms_std)
print("Price in $1000's: %.3f" % sc_y.inverse_transform(price_std))

# now let's use the scikit model for regression
from sklearn.linear_model import LinearRegression


slr = LinearRegression()
slr.fit(X, y)
y_pred = slr.predict(X)
print('Slope: %.3f' % slr.coef_[0])
print('Intercept: %.3f' % slr.intercept_)

lin_regplot(X, y, slr)
plt.xlabel('Average number of rooms [RM]')
plt.ylabel('Price in $1000\'s [MEDV]')
plt.tight_layout()
# plt.savefig('./figures/scikit_lr_fit.png', dpi=300)
plt.show()

# we can also calculate the coefficients using the normal equation model
# adding a column vector of "ones"
Xb = np.hstack((np.ones((X.shape[0], 1)), X))
w = np.zeros(X.shape[1])
z = np.linalg.inv(np.dot(Xb.T, Xb))
w = np.dot(z, np.dot(Xb.T, y))

print('Slope: %.3f' % w[1])
print('Intercept: %.3f' % w[0])

# oftentimes you have to deal with very bad outliers
# sometines you can just throw them out
# another approach is to use RANSAC
# RANSAC - Random Sample Concensus
# basically this method fits the model into the subset of data, called inliers
# we can summarize the algorithm as follows:
# 1. select the random number of samples, inliers, and fit the model
# 2. test all other samples against the model and add those points that fall within tolerance to inliers
# 3. refit the model using all inliers
# 4. estimate the error of the fitted model versu the inliers
# 5. Terminate the algorithm if the performance meets a certain user-defined threshold or if a
#    fixed number of iterations has been reached; go back to step 1 otherwise.

from sklearn.linear_model import RANSACRegressor


ransac = RANSACRegressor(LinearRegression(),
                         max_trials=100,
                         min_samples=50,
                         residual_metric=lambda x: np.sum(np.abs(x), axis=1),
                         residual_threshold=5.0,
                         random_state=0)
print(np.sum(np.abs(X), axis=1))

ransac.fit(X, y)

inlier_mask = ransac.inlier_mask_
outlier_mask = np.logical_not(inlier_mask)

ine_X = np.arange(3, 10, 1)
line_y_ransac = ransac.predict(line_X[:, np.newaxis])
plt.scatter(X[inlier_mask], y[inlier_mask], c='blue', marker='o', label='Inliers')
plt.scatter(X[outlier_mask], y[outlier_mask], c='lightgreen', marker='s', label='Outliers')
plt.plot(line_X, line_y_ransac, color='red')
plt.xlabel('Average number of rooms [RM]')
plt.ylabel('Price in $1000\'s [MEDV]')
plt.legend(loc='upper left')

plt.tight_layout()
# plt.savefig('./figures/ransac_fit.png', dpi=300)
plt.show()

print('Slope: %.3f' % ransac.estimator_.coef_[0])
print('Intercept: %.3f' % ransac.estimator_.intercept_)
