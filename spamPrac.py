# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 11:00:26 2018

@author: tejas
"""

import os
import pandas as pd
import numpy as np
from textblob import TextBlob as tb
from nltk.corpus import stopwords
from string import punctuation
from collections import Counter
##Set directory
path="C:/F/NMIMS/DataScience/Sem-3/TA/data/New folder"
os.chdir(path)

##Read CSV
spam_data = pd.read_csv("spam.csv", encoding="latin-1")
spam_data.info()
spam_data.head(3)

spam_data.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], 1 , inplace=True)
spam_data.rename(columns={'v1':'Status', 'v2':'Message'}, inplace=True)
spam_data["Status"] = spam_data["Status"].replace({'ham':0, 'spam':1})

custom=set(stopwords.words('english'))      
           
def make_dict():
    custom=set(stopwords.words('english'))
    words=[]
    for x in spam_data["Message"]:
        blob = tb(x).lower()
        words+=[word for word in list(blob.words) if word not in custom and word.isalpha()]
    dictionary = Counter(words)
    return dictionary
        


# =============================================================================
# def make_dict():
#     custom=set(stopwords.words('english'))
#     words=[]
#     for x in spam_data["Message"]:
#         print("x--------------")
#         print(x)
#         #blob = tb(x).correct().lower()
#         blob = tb(x).lower()
#         words+=[word for word in list(blob.words) if word not in custom and word.isalpha()]
#         dictionary = Counter(words)
#         len(dictionary)
#         return dictionary.most_common()
# =============================================================================

dct = make_dict()
print(dct)
print(type(dct))

def make_matrix(dictn):
    features = []
    labels = []
    for txt in spam_data["Message"]:
        data = []
        words = []
        words += txt.split(" ")
        for entry in dictn:
            data.append(words.count(entry[0]))
        features.append(data)
    labels = spam_data["Status"]
    return features, labels

features, labels = make_matrix(dct)
len(features)

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)
nb_classifier = MultinomialNB()
nb_classifier.fit(X_train, y_train)
preds = nb_classifier.predict(X_test)
acc = metrics.accuracy_score(y_test, preds)
print(acc)
cm = metrics.confusion_matrix(y_test, preds, labels=[0,1])
print(cm)
        
        



        
    



