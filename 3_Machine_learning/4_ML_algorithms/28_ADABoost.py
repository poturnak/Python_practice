#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

# AdaBoost is short for adaptive boosting

# In boosting the ensemble consists of very basic classifiers that are a bit better than random classifying
# Typically these basic classifiers are called weak learners

# The boosting procedure is summarized in the following steps:
#  - Draw a random subset d1 without replacement from the training set D to train weak learner C1
#  - Draw second random subset d2 without replacement from teh training set and add 50 samples
#    that were previously miscalssified to train a weak learner C2
#  - Find the training samples d3 in the training set D on which C1 and C2 disagree to train the third learner C3
#  - Combine the weak learners C1, C2, and C3 using the majority voting

# Boosting can lead to decrease in bias as well as variance compared to bagging models
# In contrast to the general boosting described above, AdaBoost uses the complete training set to
# trian the weak learners where the training samples are re-weighted in each interation to build the strong classifier
# that learns from the previous mistakes

# Now, let's try to create the pseudocode for AdaBoost
# 1. Set the vector w to uniform weights, where sum(wi) = 1
# 2. For j in m boosting rounds do the following
# 3. Train a weak learner Cj = train(X, y, w)
# 4. Predict class labels ~y = predict(Cj, X)
# 5. Compute weigted error err = w * (~y == y)
# 6. Compute coefficient alpha = 0.5 * log((1- err) / err)
# 7. Update weights w := w * exp(-alphaj * ~y * y)
# 8. Normalize weights to sum to 1, w := w / sum(wj)
# 9. Compute final prediction ~y = (sum(alpha*predict(Cj, X))>0)

# Now let's try to build the AdaBoost classifier

import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import accuracy_score
import numpy as np

df_wine = pd.read_csv('https://archive.ics.uci.edu/ml/'
                      'machine-learning-databases/wine/wine.data',
                      header=None)

df_wine.columns = ['Class label', 'Alcohol', 'Malic acid', 'Ash',
                   'Alcalinity of ash', 'Magnesium', 'Total phenols',
                   'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins',
                   'Color intensity', 'Hue', 'OD280/OD315 of diluted wines',
                   'Proline']

# drop 1 class
df_wine = df_wine[df_wine['Class label'] != 1]

y = df_wine['Class label'].values
X = df_wine[['Alcohol', 'Hue']].values

from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import train_test_split

le = LabelEncoder()
y = le.fit_transform(y)

X_train, X_test, y_train, y_test =\
            train_test_split(X, y,
                             test_size=0.40,
                             random_state=1)

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier

tree = DecisionTreeClassifier(criterion='entropy',
                              max_depth=1,
                              random_state=0)

ada = AdaBoostClassifier(base_estimator=tree,
                         n_estimators=500,
                         learning_rate=0.1,
                         random_state=0)

tree = tree.fit(X_train, y_train)
y_train_pred = tree.predict(X_train)
y_test_pred = tree.predict(X_test)

tree_train = accuracy_score(y_train, y_train_pred)
tree_test = accuracy_score(y_test, y_test_pred)
print('Decision tree train/test accuracies %.3f/%.3f'
      % (tree_train, tree_test))

ada = ada.fit(X_train, y_train)
y_train_pred = ada.predict(X_train)
y_test_pred = ada.predict(X_test)

ada_train = accuracy_score(y_train, y_train_pred)
ada_test = accuracy_score(y_test, y_test_pred)
print('AdaBoost train/test accuracies %.3f/%.3f'
      % (ada_train, ada_test))

x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))

f, axarr = plt.subplots(1, 2, sharex='col', sharey='row', figsize=(8, 3))


for idx, clf, tt in zip([0, 1],
                        [tree, ada],
                        ['Decision Tree', 'AdaBoost']):
    clf.fit(X_train, y_train)

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    axarr[idx].contourf(xx, yy, Z, alpha=0.3)
    axarr[idx].scatter(X_train[y_train == 0, 0],
                       X_train[y_train == 0, 1],
                       c='blue', marker='^')
    axarr[idx].scatter(X_train[y_train == 1, 0],
                       X_train[y_train == 1, 1],
                       c='red', marker='o')
    axarr[idx].set_title(tt)

axarr[0].set_ylabel('Alcohol', fontsize=12)
plt.text(10.2, -1.2,
         s='Hue',
         ha='center', va='center', fontsize=12)

plt.tight_layout()
# plt.savefig('./figures/adaboost_region.png',
#           dpi=300,
#           bbox_inches='tight')
plt.show()