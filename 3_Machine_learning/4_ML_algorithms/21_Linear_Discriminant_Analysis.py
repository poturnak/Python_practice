#! /library/Frameworks/Python.framework/Versions/3.5/python3.53

# LDA is analogous to PCA
# LDA tries to find discriminants that optimize the class separability
# LDA is an unsupervised algorithm, whereas PCA is supervised

# The assumption for LDA is that data is normally distributed
# We also assume that the classes have similar covariances and that features are statistically independent

# Here are the key steps for LDA:
# 1. Standardize the d-dimentional dataset
# 2. For each class compute d-dimensional mean vector
# 3. Construct the between class scatter matrix Sb, and within class scatter matrix Sw
# 4. Compute the eigenvectors and eigenvalues of the matrix S-1w * Sb
# 5. Choose k eignevectors that correspond to the largest eigenvalues to construct d*k transformation matrix
# 6. Project the features onto the new subspace

from matplotlib.colors import ListedColormap
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
from sklearn.lda import LDA

def plot_decision_regions(X, y, classifier, resolution=0.02, test_idx=None):
    # setup marker generator and color map
    markers = ('s', 'x', 'v', 'o', '^')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # plot class samples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1], alpha=0.8, c=cmap(idx), marker=markers[idx], label=cl)


# Get the dataset and standardize it
df_wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)
X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.fit_transform(X_test)

lda = LDA(n_components=2)
X_train_lda = lda.fit_transform( X_train_std, y_train)

lr = LogisticRegression()
lr = lr.fit(X_train_lda, y_train)
plot_decision_regions(X_train_lda, y_train, classifier=lr)
plt.xlabel('LD 1')
plt.ylabel('LD 2')
plt.legend( loc='lower left')
plt.show()
