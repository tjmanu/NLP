# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 12:15:52 2018

@author: tejas
"""

import nltk
from nltk.corpus import stopwords
from string import punctuation
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import PorterStemmer
from textblob import TextBlob as tb
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
http = urllib3.PoolManager()
response = http.request('GET',"https://timesofindia.indiatimes.com/india/rbi-governor-met-pm-modi-fm-jaitley-last-week-in-bid-to-heal-rift/articleshow/66597760.cms")
soup = BeautifulSoup(response.data, 'html.parser')
Text = ". ".join([p.text for p in soup.find_all('div', {'class':'Normal'})])
print(Text)
psm = PorterStemmer()
st = LancasterStemmer()
lmtzr=WordNetLemmatizer()
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
from collections import Counter
counts = Counter(stemmed_words)
print(counts)

def score(sent):
    words = word_tokenize(sent)
    score = [counts[x] for x in words]
    return sum(score)

scores = [score(sent) for sent in sent_tokenize(stemmed_para)]
print(scores)

most_comm=counts.most_common(5)
print(most_comm)

from gensim.corpora.dictionary import Dictionary
words=[lmtzr.lemmatize(word.lower()) for word in word_tokenize(Text) if word.isalpha()]
words_rem=[word for word in words if word not in custom]
dictnry = Dictionary([words_rem])
corp = [dictnry.doc2bow(article) for article in [words_rem]]
##print(dictnry.doc2bow([words_rem]))

import gensim
Lda = gensim.models.ldamodel.LdaModel
ldamodel = Lda(corp, num_topics=3, id2word = dictnry, passes=50)
####Topic
print(ldamodel.print_topics(num_topics=3, num_words=3))
