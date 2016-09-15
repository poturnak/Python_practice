#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

# One of the most used metrics is the model accuracy (how well it classifies the test data)
# However, there are other metrics as well, such as precision, recall, and F1 score

# we can also build the confusion matrix
# this matrix will depend on which class is positive and which is negative
# in the case below, 1 means there is alert, 0 means there is no alert
# !!!!!! remember that the positive class in scikit learn is 1, same as on the picture below

#                   Predicted class
#               1                   0
#        1   True positive       False negative
#
# Actual
# Class
#        0   False positive      True negative
#
#
# Now we can take a look at how we calculate the metrics
# Error = (FP + FN) / (FP + FN + TP + TN)
# Accuracy = 1 - Error
#
# False positive rate
# FPR = FP / (FP + TN) (how many items we picked from all irrelevant items)
#
# True positive rate
# TPR = TP / (TP + FN) (same as recall)
#
# Precision
# PRE = TP / (TP + FP) (how many of the selected items are relevant, meaning how many are actual alerts)
#
# Recall
# REC = TP / (TP + FN) (how many of the relevant items were selected, meaning how many alerts we picked)
#
# F1 score
# F1 = 2 * (PRE * REC) / (PRE + REC)

from matplotlib import pyplot as plt
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import train_test_split
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data',
                 header=None)
X = df.loc[:, 2:].values
y = df.loc[:, 1].values
le = LabelEncoder()
y = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)
pipe_svc = Pipeline([('scl', StandardScaler()),('clf', SVC(random_state=1))])
pipe_svc.fit(X_train, y_train)
y_pred = pipe_svc.predict(X_test)
confmat = confusion_matrix(y_true=y_test, y_pred=y_pred)
print(confmat)

fig, ax = plt.subplots(figsize=(2.5, 2.5))
ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.3)
for i in range(confmat.shape[0]):
    for j in range(confmat.shape[1]):
        ax.text(x=j, y=i, s=confmat[i, j], va='center', ha='center')

plt.xlabel('predicted label')
plt.ylabel('true label')

plt.tight_layout()
# plt.savefig('./figures/confusion_matrix.png', dpi=300)
plt.show()

print('Precision: %.3f' % precision_score(y_true=y_test, y_pred=y_pred))
print('Recall: %.3f' % recall_score(y_true=y_test, y_pred=y_pred))
print('F1: %.3f' % f1_score(y_true=y_test, y_pred=y_pred))