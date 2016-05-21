#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# Conveniently Iris dataset is already available as part of scikit learn

from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap

iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target  # in this dataset the labels are stored as 0, 1, 2 for three flower classes

# now let's split the dataset into the training and testing datasets
# this method shuffles the array and splits it into parts
# 30% (45 samples) will go into the test set, 70% (105 samples) will go into training set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# now let's standardize the data values (subtract the mean and divide by std)
sc = StandardScaler()  # initialize the new object of standardization class
sc.fit(X_train)  # fit method estimated the mean and std from the whole dataset for each dimension
print('The means for standardization', sc.mean_)  # print the array of means for each feature
print('The variance for standardization', sc.var_)  # print the array of variances for each feature
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)  # we use the same parameters to standardize test set so that values are comparable

# now let's train the Perceptron class
# ove vs all method will be used so that we can feed tree classes to Perceptron
ppn = Perceptron(n_iter=5, eta0=0.1, random_state=0)
ppn.fit(X_train_std, y_train)

# Having trained the Perceptron we can now make predictions using predict method
# We can do manual calculations
y_pred = ppn.predict(X_test_std)
print(y_pred)
# print('Misclassified samples: {}'.format((y_test != y_pred).sum()))
# print('Classification accuracy: {}'.format((len(y_test) - (y_test != y_pred).sum())/len(y_test)))

# we can also calculate prediction accurace using scikit
acc = accuracy_score(y_test, y_pred)
print('Accuracy score: {0:4.3f}'.format(acc))

# Now we will plot the regions using out contour plto function

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
# _________________________________________________________________________________________________________________
X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))
plot_decision_regions(X_combined_std, y_combined, classifier=ppn, test_idx=range(105, 150))
plt.xlabel('petal length [std]')
plt.ylabel('petal width [std]')
plt.legend(loc='upper left')
plt.show()
