# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 10:05:45 2018

@author: tejas
"""

import urllib.request 
link = "https://economictimes.indiatimes.com/industry/banking/finance/banking/4-public-sector-banks-may-come-out-of-pca-shackles/articleshow/66550721.cms"

req = urllib.request.Request(link)
response = urllib.request.urlopen(req)
the_page = response.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(the_page, 'lxml')

paras = ' '.join([p.text for p in soup.findAll('p')])
print (paras)

text = (paras[:-390])
print (text)

from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
sents = sent_tokenize(text)
print (sents)

print (len(sents))
words = word_tokenize(text)
print (len(words))
print (words)

from nltk.corpus import stopwords
from string import punctuation
custom = set(stopwords.words('english')+list(punctuation))

words = [word for word in words if word not in custom]
print (len(words))

counts = Counter(words)
counts = counts.most_common()
print (counts)

final_words_we_need = [x for x in counts if x[1]>3]
final_words_we_need

d = {}
for s in sents:
    score = 0
    for w in final_words_we_need:
        if w[0] in s:
            score = score +w[1]
    d[s] = score
import operator
sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse = True)
sorted_d

our_summary = []
for x in sorted_d[:6]:
    our_summary.append(x[0])
our_summary = ''.join(our_summary[:])
print (our_summary)