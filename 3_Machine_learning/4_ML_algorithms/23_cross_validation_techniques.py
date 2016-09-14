#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

# first we will take a look at the holdout cross-validation technique
# this is a simple technique to split the data set into 3 pieces:
#  - training set - used to fit different models
#  - validation set - used to tweak different paramaters of a model
#  - test set - finally test our model on the real data

# Now we are going to look at the k-fold cross-validation
# here we randomely split the data set into k folds without replacement
# k-1 folds are used to train the model
# 1 fold is used for testing

# in k-fold cross-validation, the original sample is randomly partitioned into k equal sized subsamples.
# Of the k subsamples, a single subsample is retained as the validation data for testing the model,
# and the remaining k − 1 subsamples are used as training data.
# The cross-validation process is then repeated k times (the folds),
# with each of the k subsamples used exactly once as the validation data.
# The k results from the folds can then be averaged to produce a single estimation.
# The advantage of this method over repeated random sub-sampling (see below) is that all observations
# are used for both training and validation, and each observation is used for validation exactly once.
# 10-fold cross-validation is commonly used,[6] but in general k remains an unfixed parameter.

# When k=n (the number of observations), the k-fold cross-validation is exactly the leave-one-out cross-validation.

# In stratified k-fold cross-validation, the folds are selected so that the mean
# response value is approximately equal in all the folds. In the case of a dichotomous classification,
# this means that each fold contains roughly the same proportions of the two types of class labels.


