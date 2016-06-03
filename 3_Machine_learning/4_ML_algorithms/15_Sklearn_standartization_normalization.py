#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
from sklearn.preprocessing import MinMaxScaler
from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

df_wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)
df_wine.columns = ['Class label', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols',
                   'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue',
                   'OD280/ OD315 of diluted wines', 'Proline']
X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Normalization - bringing all the features onto the scale [0, 1]
# for normalization we can use min max scaler
# x_norm = (x - x_min) / (x_max - x_min)
mms = MinMaxScaler()
X_train_norm = mms.fit_transform(X_train)
X_test_norm = mms.transform(X_test)

# Standartization - center all the features around mean 0 and std of 1
# x_std = (x - mean) / std
stdsc = StandardScaler()
X_train_std = stdsc.fit_transform(X_train)
X_test_std = stdsc.transform(X_test)


