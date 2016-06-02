#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# Here is how the algorithm will work
# 1. Choose the number of k and a distance metric.
# 2. Find the k nearest neighbors of the sample that we want to classify.
# 3. Assign the class label by majority vote.
# Great thing about this algorithm is that we can adapt as we learn more data.

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
from sklearn.neighbors import KNeighborsClassifier

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

# now let's standardize the data values (subtract the mean and divide by std)
sc = StandardScaler()  # initialize the new object of standardization class
sc.fit(X_train)  # fit method estimated the mean and std from the whole dataset for each dimension
print('The means for standardization', sc.mean_)  # print the array of means for each feature
print('The variance for standardization', sc.var_)  # print the array of variances for each feature
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)  # we use the same parameters to standardize test set so that values are comparable
X_combined_std = np.vstack((X_train_std, X_test_std))

knn = KNeighborsClassifier(n_neighbors=5, p=2, metric='minkowski')
# p is basically the power to which to raise the difference in coordinates
knn.fit(X_train_std, y_train)
plot_decision_regions(X_combined_std, y_combined, classifier=knn, test_idx=range(105, 150))
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.show()