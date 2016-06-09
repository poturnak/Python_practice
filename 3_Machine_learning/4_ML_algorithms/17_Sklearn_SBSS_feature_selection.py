#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# We can also reduce complexity of the model by applying dimensionality reduction
# There are 2 types:
#  - feature selection (select the features to use)
#  - feature extraction (construct new features from the existing ones)

# In the example we will take a look at sequential feature selection algorithm
# The classic algorithm is the SBS (Sequential Backward Selection)
# 1. Initialize algorithm with k=d (d is dimensionality of full space, k is desired space)
# 2. Determine the feature which removal causes least loss (the highest accuracy score)
# 3. Remove the feature from the dataset
# 4. Repeat until we reach desired k

from sklearn.base import clone
from itertools import combinations
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


class SBS:
    def __init__(self, estimator, feature_lim, test_size = 0.25, random_state=0):
        self.estimator = clone(estimator)
        self.feature_lim = feature_lim
        self.test_size = test_size
        self.random_state = random_state
        self.best_scores = []
        self.best_combinations = []

    def predict(self, X_train, y_train, X_test, y_test):
        self.estimator.fit(X_train, y_train)
        y_pred = self.estimator.predict(X_test)
        score = accuracy_score(y_test, y_pred)
        return score

    def fit(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.test_size, random_state=self.random_state)
        dimensions = X_train.shape[1]
        combination = range(dimensions)

        while dimensions > self.feature_lim:
            scores = []
            features = []
            for i in combinations(combination, r=dimensions):
                scores.append(self.predict(X_train[:, i], y_train, X_test[:, i], y_test))
                features.append(i)
            print(scores)
            self.best_scores.append(max(scores))
            self.best_combinations.append(features[np.argmax(scores)])
            dimensions -= 1
            combination = features[np.argmax(scores)]

# ______________________________________________________________________________________________________________________
df_wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)
df_wine.columns = ['Class label', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols',
                   'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue',
                   'OD280/ OD315 of diluted wines', 'Proline']
X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Standartization - center all the features around mean 0 and std of 1
# x_std = (x - mean) / std
stdsc = StandardScaler()
X_train_std = stdsc.fit_transform(X_train)
X_test_std = stdsc.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=2)
sbs = SBS(knn, feature_lim=1)
sbs.fit(X_train_std, y_train)

k_feat = [len(k) for k in sbs.best_combinations]
plt.plot(k_feat, sbs.best_scores, marker ='o')
plt.ylim([0.7, 1.1])
plt.ylabel('Accuracy')
plt.xlabel('Number of features')
plt.grid()
plt.show()



# class SBS:
#     def __init__(self, estimator, k_features, scoring=accuracy_score, test_size=0.25, random_state=0):
#         self.scoring = scoring
#         self.estimator = clone(estimator)
#         self.k_features = k_features
#         self.test_size = test_size
#         self.random_state = random_state
#
#     def fit(self, X, y):
#         X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.test_size, random_state=self.random_state)
#         dim = X_train.shape[1]
#         self.indices_ = tuple(range(dim))
#         self.subsets_ = [self.indices_]
#         score = self._calc_score(X_train, y_train, X_test, y_test, self.indices_)
#         self.scores_ = [score]
#
#         while dim > self.k_features:
#             scores = []
#             subsets = []
#
#             for p in combinations(self.indices_, r=dim-1):
#                 score = self._calc_score(X_train, y_train, X_test, y_test, p)
#                 scores.append(score)
#                 subsets.append(p)
#
#             best = np.argmax(scores)
#             self.indices_ = subsets[best]
#             self.subsets_.append(self.indices_)
#
#             dim -= 1
#             self.scores_.append(scores[best])
#         self.k_score_ = self.scores_[-1]
#
#         return self
#
#     def transform(self, X):
#         return X[:, self.indices_]
#
#     def _calc_score(self, X_train, y_train, X_test, y_test, indices):
#         self.estimator.fit(X_train[:, indices], y_train)
#         y_pred = self.estimator.predict(X_test[:, indices])
#         score = self.scoring(y_test, y_pred)
#         return score
# _____________________________________________________________________________________________________________



