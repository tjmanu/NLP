# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 13:43:54 2018

@author: tejas
"""

from nltk import pos_tag
from nltk.corpus import stopwords
from string import punctuation
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import PorterStemmer
psm = PorterStemmer()
st = LancasterStemmer()
lmtzr=WordNetLemmatizer()

Text="I am planning to visit New Delhi to attend Analytics Vidhya Delhi Hackathon"
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



words_2=[word for word in word_tokenize(Text) if word not in custom]
count_words2=Counter(words_2)
noun=[token for token, pos in pos_tag(word_tokenize(Text)) if pos.startswith('N')]      
print(noun)

verb=[token for token, pos in pos_tag(word_tokenize(Text)) if pos.startswith('V')]      
print(verb)

for w in count_words2:
    if count_words2[w]>1:
        print(w)
        
        