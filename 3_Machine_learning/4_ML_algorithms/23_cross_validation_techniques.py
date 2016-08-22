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

# Here is how we will use the system:
#  - split the data set into folds (say 10), 9 are used to train, 1 is used to test
#  - randomly choose the test fold, train the model on the remaining 9, test using test fold, estimate parameter
#  - tune the parameters of the model
#  - repeat the previous step
#  - repeat until we tested all parameters
#  - choose the model parameters
#  - train the model again using 80% of the data set, test using remaining 20%

