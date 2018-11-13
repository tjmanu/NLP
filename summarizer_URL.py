# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:59:13 2018

@author: tejas
"""

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
http = urllib3.PoolManager()
response = http.request('GET',"https://timesofindia.indiatimes.com/india/rbi-governor-met-pm-modi-fm-jaitley-last-week-in-bid-to-heal-rift/articleshow/66597760.cms")
soup = BeautifulSoup(response.data, 'html.parser')
Text = ". ".join([p.text for p in soup.find_all('div', {'class':'Normal'})])
print(Text)

from nltk.corpus import stopwords
from string import punctuation
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import PorterStemmer
psm = PorterStemmer()
st = LancasterStemmer()
lmtzr=WordNetLemmatizer()
orignal_sentences = sent_tokenize(Text)
print(orignal_sentences)

paras_stemmedSansStopWords = [psm.stem(word.lower()) for word in word_tokenize(Text) if word.lower() not in stopwords.words('english')]
print(paras_stemmedSansStopWords)

stemmed_para = " ".join([word for word in paras_stemmedSansStopWords])
stemmed_para

custom = set(stopwords.words('english')+list(punctuation) + ["'",'"',"“",'’'])
stemmed_words = [word for word in paras_stemmedSansStopWords if word not in custom]
print(stemmed_words)
print(stopwords.words('english'))


from collections import Counter
counts = Counter(stemmed_words)
print(counts)

def score(sent):
    words = word_tokenize(sent)
    score = [counts[x] for x in words]
    return sum(score)

scores = [score(sent) for sent in sent_tokenize(stemmed_para)]
print(scores)

threshold = sorted(scores)[-4]
for i,x in enumerate(scores):
    if x > threshold:
        print(orignal_sentences[i])  
