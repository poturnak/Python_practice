#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# with the decision tree we start at the root of the tree and then we split the data based on the feature
# that gives us the largest information gain
# in order not to overfit you will define the maximum tree depth

# Here is the objective function that will maximize the infomration gain at each split
# IG = I(Dp) - sum(j=1, m)(Nj/Np * I(DJ))
# I - impurity measure
# Np - total number os members in the parent node
# Nj - total number of members in the jth child node
# Therefore, on the high level, total infomration gain is the difference between parent node impurity and
# the impurity of the child nodes combined

# Now, the three impurity measures that are used are:
# 1. Entropy
#   Ent(t) = -sum(i=1, c)(p(i|t) * log2 p(i|t))
#   For 2 classes the entropy is the following:
#   Ent(t) = -p * np.log2(p) - (1 - p) * np.log2((1 - p))
#   p(i|t) - is the proportion of the samples that belongs to class c for a particular node t
#   Therefore, entropy is the highest if we have uniform distribution
#   Entropy is 0 if we have all samples belonging to the same class
#   As a result, entropy tries to maximize the mutual infomration in the tree
#
# 2. Gini impurity
#   Gini(t) = sum(i=1, c) (p(i|t) * (1 - p(i|t))
#   Therefore, Gini impurity tries to minimize the possibility of misclassification
#   Again, if the classes are perfectly mixed, the Gini impurity is maximal, it will be 0.5
#
# 3. Classification Error
#   Error = 1 - max(p(i|t))

import numpy as np
from matplotlib import pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn import datasets
from matplotlib.colors import ListedColormap
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

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

tree = DecisionTreeClassifier(criterion='entropy', random_state=0)
tree.fit(X_train, y_train)
X_combined = np.vstack((X_train, X_test))
y_combined = np.hstack((y_train, y_test))
plot_decision_regions(X_combined, y_combined, classifier=tree, test_idx=range(105, 150))
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.legend(loc='upper left')
plt.show()

export_graphviz(tree, out_file='tree.dot', feature_names=['petal length', 'petal width'])