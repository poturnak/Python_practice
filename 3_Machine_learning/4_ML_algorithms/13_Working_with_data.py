#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

import pandas as pd
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







