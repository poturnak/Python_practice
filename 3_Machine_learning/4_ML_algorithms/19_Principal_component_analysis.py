#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

# PCA is an unsupervised linear transformation technique that is used for dimensionality reduction
# Once we do PCA we need to standardize the features for our analysis

# Here are the steps to perform PCA analysis
# 1. Standardize the d dimensional dataset
# 2. Construct the covariance matrix
# 3. Decompose the covariance matrix into its eignevectors and its eigenvalues
# 4. Select k eignevectors that correspond to the k latgest eignevalues, where k is dimensionality of the new space
# 5. Construct a projection matrix W from the top eigenvectors
# 6. Transform the d dimensional input dataset using the projection matrix W

import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

df_wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)
X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.fit_transform(X_test)

# when looking or covariance matrix, the positive covariance means features increase or decrease together
# negative covariance shows the opposite
# covariance formula 1/n * sum((x - xmean) * (y - ymean))
# in our example the means are zero since we standardized the features

cov_mat = np.cov(X_train_std.T)
eigen_vals, eigen_vecs = np.linalg.eig(cov_mat)
print(eigen_vals)
# eignevectors are stored as columns in the eigen_vecs matrix
# now let's calculate and plot variance explained ratios
# that is the ratio eigenvalue / sum of all eigenvalues

tot = sum(eigen_vals)
var_exp = [i / tot for i in sorted(eigen_vals, reverse=True)]
cum_var_exp = np.cumsum(var_exp)
print(cum_var_exp)
import matplotlib.pyplot as plt
plt.bar(range(1, 14), var_exp, alpha=0.5, align='center', label='individual explained variance')
plt.step(range(1, 14), cum_var_exp, where='mid', label='cumulative explained variance')
plt.ylabel('Explained variance ratio')
plt.xlabel('Principal components')
plt.legend(loc='best')
plt.show()

eigen_pairs=[(np.abs(eigen_vals[i]), eigen_vecs[:, i]) for i in range(len(eigen_vals))]
eigen_pairs.sort(reverse=True)

w = np.hstack((eigen_pairs[0][1][:, np.newaxis], eigen_pairs[1][1][:, np.newaxis]))
print('Matrix W:\n', w)

# now we can transform the original values into the new 2 dimentional space
X_train_pca = X_train_std.dot(w)

colors = ['r', 'b', 'g']
markers = ['s', 'x', 'o']
for l, c, m in zip(np.unique(y_train), colors, markers):
    plt.scatter(X_train_pca[ y_train == l, 0], X_train_pca[y_train == l, 1], c=c, label=l, marker=m)
plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.legend(loc='lower left')
plt.show()
