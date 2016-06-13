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
    def __init__(self, estimator, feature_lim, test_size=0.25, random_state=0):
        self.estimator = clone(estimator)
        self.feature_lim = feature_lim
        self.test_size = test_size
        self.random_state = random_state
        self.best_scores = []
        self.best_combinations = []

    def calc_score(self, x, y, test_x, test_y):
        self.estimator.fit(x, y)
        pred_y = self.estimator.predict(test_x)
        score = accuracy_score(test_y, pred_y)
        return score

    def fit(self, x, y):
        train_x, test_x, train_y, test_y = \
            train_test_split(x, y, test_size=self.test_size, random_state=self.random_state)
        dimensions = train_x.shape[1]
        print(dimensions)
        combination = list(range(dimensions))
        print(combination)

        while dimensions > self.feature_lim:
            scores = []
            features = []
            for i in combinations(combination, r=dimensions):
                scores.append(self.calc_score(train_x[:, i], train_y, test_x[:, i], test_y))
                features.append(i)
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

# Standardization - center all the features around mean 0 and std of 1
# x_std = (x - mean) / std
stdsc = StandardScaler()
X_train_std = stdsc.fit_transform(X_train)
X_test_std = stdsc.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=2)
sbs = SBS(knn, feature_lim=1, random_state=0)
sbs.fit(X_train_std, y_train)

k_feat = [len(k) for k in sbs.best_combinations]
plt.plot(k_feat, sbs.best_scores, marker ='o')
plt.ylim([0.7, 1.1])
plt.ylabel('Accuracy')
plt.xlabel('Number of features')
plt.grid()
plt.show()

# Now let's evaluate the performance of our KNN classifier using all features
knn.fit(X_train_std, y_train)
print('Training accuracy:', knn.score(X_train_std, y_train))
print('Test accuracy:', knn.score(X_test_std, y_test))

# Now let's use only 7 features that we selected to evaluate the KNN performance
print('Features to choose: ', sbs.best_combinations[6])
features7 = sbs.best_combinations[6]
knn.fit(X_train_std[:, features7], y_train)
print('Training accuracy:', knn.score(X_train_std[:, features7], y_train))
print('Test accuracy:', knn.score(X_test_std[:, features7], y_test))


