#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
# Naive bayes classifier
clf = GaussianNB()
# Training
t0 = time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"

# Predict on test set
t0 = time()
labels_test_predicted = clf.predict(features_test)
print "prediction time:", round(time()-t0, 3), "s"

# Predict on train set
labels_train_predicted = clf.predict(features_train)
# Accuracy
train_acc = accuracy_score(labels_train,labels_train_predicted)
test_acc = accuracy_score(labels_test,labels_test_predicted)
print("Train acuracy {}".format(train_acc))
print("Test acuracy {}".format(test_acc))

#########################################################


