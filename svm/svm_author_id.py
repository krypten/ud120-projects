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

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

from sklearn.svm import SVC

clf = SVC(C=10000.0, gamma='auto', kernel='rbf')
t0 = time()
clf = clf.fit(features_train, labels_train)
t1 = time()
print (round(t1 - t0))
pred = clf.predict(features_test)
t2 = time()
print (round(t2 - t1))

import collections
print(collections.Counter(pred)[1])

from sklearn.metrics import accuracy_score
print (accuracy_score(pred, labels_test))





