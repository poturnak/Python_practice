#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

import pandas as pd
import numpy as np
from io import StringIO
from sklearn.preprocessing import Imputer

csv_data = '''A,B,C,D
1.0,2.0,3.0,4.0
5.0,6.0,,8.0
0.0,11.0,12.0,'''
df = pd.read_csv(StringIO(csv_data))
print(df)
print(type(df))

# now we can check if some of the values are missing
print(df.isnull().sum())

# pandas object is the dataframe, we can access the numpy array by using
print(df.values)

# we can eliminate the samples with missing values
print(df.dropna())
# or we can eliminate the features with missing values
print(df.dropna(axis=1))
# dropna can also support other parameters
#  - df.dropna(how='all) - only drop rows where all values are NaN (not a number)
#  - df.dropna(thresh=4) - drop rows where we have at least 4 NaNs
#  - df.dropna(subset=['C']) - drop rows where NaN appears in the specific column (C here)

# Sometimes we can use the technique 'mean imputation'
# we will replace the missing values with the mean of the entire column
imr = Imputer(missing_values='NaN', strategy='mean', axis=0)
imr = imr.fit(df)
imputed_data = imr.transform(df.values)
print(imputed_data)

# Now, we are going to take a look at how we are going to handle categorical data
# There can be numerical data or categorical data
# Categorical can be:
#  - ordinal - values that can be further sorted or compared (T shirt sizes for example)
#  - nominal - values that can not be sorted or compared (colors fo T shirst for example)

df1 = pd.DataFrame([
    ['green', 'M', 10.1, 'class1'],
    ['red', 'L', 13.5, 'class2'],
    ['blue', 'XL', 15.3, 'class1']
])
df1.columns = ['color', 'size', 'price', 'classlabel']

# we can map ordinal features
# we can create the mapping manually
size_mapping = {'XL': 3, 'L': 2, 'M': 1}
df1['size'] = df1['size'].map(size_mapping)
print(df1)

# if we want to transform the integers back to original values we can do inverse mapping using
inv_size_mapping = {v: k for k, v in size_mapping.items()}
print(inv_size_mapping)

# We can also encode the class labels
# a lot of algorithms require the class labels to be represented using the numbres instead of categorical values
class_mapping = {label: idx for idx, label in enumerate(np.unique(df1['classlabel']))}
df1['classlabel'] = df1['classlabel'].map(class_mapping)
print(df1)
# we can reverse the mapping using the following
inv_class_mapping = {i: j for j, i in class_mapping.items()}
df1['classlabel'] = df1['classlabel'].map(inv_class_mapping)
print(df1)

