# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 09:04:38 2018

@author: Sanmoy
"""

import os
import pandas as pd
import numpy as np
from textblob import TextBlob as tb
from nltk.corpus import stopwords
from string import punctuation
from collections import Counter
##Set directory
path="C:/F/NMIMS/DataScience/Sem-3/TA/data/"
os.chdir(path)

##Read CSV
news_data = pd.read_csv("fake_or_real_news.csv", encoding="latin-1")
news_data.info()
news_data.head(3)

from sklearn.model_selection import train_test_split as tts
from sklearn.feature_extraction.text import CountVectorizer
#x = news_data['text']
y = news_data['label']

x_train, x_test, y_train, y_test = tts(news_data['text'], y, test_size=0.30, random_state=53)
count_vectorizer = CountVectorizer(stop_words='english')
count_train = count_vectorizer.fit_transform(x_train)
count_test = count_vectorizer.transform(x_test)

from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
nb_classifier = MultinomialNB()
nb_classifier.fit(count_train, y_train)
preds = nb_classifier.predict(count_test)
acc = metrics.accuracy_score(y_test, preds)
print(acc)
cm = metrics.confusion_matrix(y_test, preds, labels=['FAKE','REAL'])
print(cm)






##############################################
import spacy
article = news_data['text'][1]
sp = spacy.load('en', parser=False, matcher=False)
doc = sp(article)
for ent in doc.ents:
    print(ent.label_, ent.text)
    
for token in doc:
    print(token.text,token.tag_)
