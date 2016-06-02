#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# 1. Draw a random bootstrap sample of size n (randomly choose n samples from the training set with replacement)
# 2. Grow a decision tree from the bootstrap sample. At each node:
#   2.1 Randomly select d features without replacement.
#   2.2 Split the node using the feature that provides the best split according to the objective function
#       for instance, by maximizing the information gain.
# 3. Repeat the steps 1 to 2 k times.
# 4. Aggregate the prediction by each tree to assign the class label by majority vote.
#
# Although random forests don't offer the same level of interpretability as decision trees, a big advantage
# of random forests is that we don't have to worry so much about choosing good hyperparameter values.
# We typically don't need to prune the random forest since the ensemble model is quite robust to noise from the
# individual decision trees. The only parameter that we really need to care about in practice is the number
# of trees k (step 3) that we choose for the random forest. Typically, the larger the number of trees, the better
# the performance of the random forest classifier at the expense of an increased computational cost.
#
# However, there are other parameters that we can optimize:
#  - number of samples we draw for each split (n)
#  - number of feature that we ramdomely choose for the analysis (d)

# Large n gives us higher variance, thus is potential to overfitting
# Smaller n gives us higher bias
# Typically n is chosen to be equal to the size of original sample
# d is chosen to be d = sqrt(m), m is the total number of features in the training dataset


import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import datasets
from matplotlib.colors import ListedColormap
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.ensemble import RandomForestClassifier

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

    # highlight test samples
    if test_idx:
        X_test, y_test = X[test_idx, :], y[test_idx]
        plt.scatter(X_test[:, 0], X_test[:, 1], c='', alpha=1.0, linewidth=1, marker='o', s=55, label='test set')


iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target  # in this dataset the labels are stored as 0, 1, 2 for three flower classes

# now let's split the dataset into the training and testing datasets
# this method shuffles the array and splits it into parts
# 30% (45 samples) will go into the test set, 70% (105 samples) will go into training set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
X_combined = np.vstack((X_train, X_test))
y_combined = np.hstack((y_train, y_test))

forest = RandomForestClassifier(criterion='entropy', n_estimators=10, random_state=1, n_jobs=2)
# n_estimators gives us the number of trees to use, in this example, 10
# n_jobs allows us to parallelize the job using the cores on the computer, here we have 2
forest.fit(X_train, y_train)
plot_decision_regions(X_combined, y_combined, classifier=forest, test_idx=range(105, 150))
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.legend(loc='upper left')
plt.show()