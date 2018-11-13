# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:53:03 2018

@author: tejas
"""
import os
import pandas as pd
import numpy as np
import seaborn as sb
os.getcwd()
os.chdir("F:/NMIMS Mtech (Sem-III)/Sentiment/enron1/emails/")

from collections import Counter
def make_dict():
    words=[]
    for email in os.listdir(os.getcwd()):
        text=open(email, encoding="latin-1")
        blob=text.read()
        words+=blob.split(" ")
    for i in range(len(words)):
        if not words[i].isalpha():
            words[i]=""
    dictionary=Counter(words)
    del dictionary[""]
    return dictionary.most_common(3000)

d=make_dict()
d

def make_dictionary(dictionary):
    features=[]
    labels=[]
    for email in os.listdir(os.getcwd()):
        data=[]
        words=[]
        text=open(email, encoding="latin-1")
        words+=text.read().split(" ")
        for entry in dictionary:
            data.append(words.count(entry[0]))
        features.append(data)
        if "ham" in email:
            labels.append(0)
        else:
            labels.append(1)
    return features,labels

features, labels= make_dictionary(d)
len(features)
len(labels)

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
import pickle as c

x_train, x_test, y_train, y_test= tts(features, labels, test_size=0.4)
clf=MultinomialNB()
clf.fit(x_train, y_train)

preds=clf.predict(x_test)
print(accuracy_score(y_test,preds))
features= []



inp= input(">").split()
for word in d:
    features.append(inp.count(word[0]))
res= clf.predict([features])
print (["Not Spam","Spam"][res[0]])




