#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Create classifier and train
clf = SVC(kernel='rbf',C=10000)
# train with smaller training set to speed up computation
#clf.fit(features_train[:len(features_train)/100],labels_train[:len(features_train)/100])
clf.fit(features_train,labels_train)

# Predict
predicted_train = clf.predict(features_train)
predicted_test = clf.predict(features_test)

# Accuracy
acc_train = accuracy_score(labels_train,predicted_train)
acc_test = accuracy_score(labels_test,predicted_test)

print("Training accuracy is {}".format(acc_train))
print("Test accuracy is {}".format(acc_test))
#########################################################


