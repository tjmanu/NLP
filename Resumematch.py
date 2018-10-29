# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:09:45 2018

@author: tejas
"""

import os
import pandas as pd
import gensim
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
custom=set(stopwords.words('english')+list(punctuation)+['â\x80¢'])
from textblob import TextBlob as tb

path="C:/F/NMIMS/DataScience/Sem-3/TA/data"
os.chdir(path)

data = open("resume.txt", encoding="latin-1").read()
doc = data.replace("\t", " ")
doc = doc.replace("\n", " ")

resume = " ".join([word for word in word_tokenize(doc) if word not in custom])
blob = tb(resume)
blob.sentences
blob.pos_tags


sent = sent_tokenize(resume)
words = word_tokenize(resume)

from collections import Counter
counts=Counter(words)
count_common=counts.most_common()
print(count_common)




resumeData = pd.read_csv("resumes-dataset-with-labels/resume_dataset.csv")
resumeData.head(6)
resumeData.iloc[:,2]
lst_resum = []
for i in resumeData.iloc[:,2]:
    lst_resum.append(i)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import operator

vocabulary = set()
for doc in lst_resum:
    vocabulary.update(doc.split())
    
vocabulary = list(vocabulary)
tfidf = TfidfVectorizer(vocabulary=vocabulary)


tfidf.fit(lst_resum)
tfidf.transform(lst_resum)

final = {}
for doc in lst_resum:
    score={}
#    print (doc)
    # Transform a document into TfIdf coordinates
    X = tfidf.transform([doc])
    for word in doc.split():
        score[word] = X[0, tfidf.vocabulary_[word]]
    sortedscore = sorted(score.items(), key=operator.itemgetter(1), reverse=True)
#    print ("\t", sortedscore)
    final[doc] = dict(sortedscore)

print(final)



count_vectorizer = CountVectorizer()
count_vectorizer.fit_transform(sent)
