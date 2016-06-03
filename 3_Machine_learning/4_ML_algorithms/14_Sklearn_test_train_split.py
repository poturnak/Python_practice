#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split

df_wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)
df_wine.columns = ['Class label', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols',
                   'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue',
                   'OD280/ OD315 of diluted wines', 'Proline']
print('Class labels', np.unique(df_wine['Class label']))
print(df_wine.head())

# now we can separate the dataset into training and test subsets
X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)




