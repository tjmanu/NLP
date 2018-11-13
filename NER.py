# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 12:05:26 2018

@author: tejas
"""

import nltk
from nltk.corpus import stopwords
from string import punctuation
from nltk.tokenize import word_tokenize, sent_tokenize
from textblob import TextBlob as tb

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
http = urllib3.PoolManager()
response = http.request('GET',"https://timesofindia.indiatimes.com/india/rbi-governor-met-pm-modi-fm-jaitley-last-week-in-bid-to-heal-rift/articleshow/66597760.cms")
soup = BeautifulSoup(response.data, 'html.parser')
Text = ". ".join([p.text for p in soup.find_all('div', {'class':'Normal'})])
print(Text)

blob=tb(Text)

#print(blob)
a=blob.tags

#print(blob.tags)
for i,x in enumerate(a):
    if a[i][1]=='NNP':
        print(a[i])

tokenized_text=word_tokenize(Text)
tagged_sent=nltk.pos_tag(tokenized_text)
chunk_sent=nltk.ne_chunk(tagged_sent)
named_entities=[]
for tagged_tree in chunk_sent:
    if hasattr(tagged_tree, 'label'):
        #print(tagged_tree)
        entity_name = ' '.join(c[0] for c in tagged_tree.leaves())
        entity_type = tagged_tree.label()
        named_entities.append((entity_name, entity_type))

print(named_entities)
locations=[]
for loc in named_entities:
    if loc[1]=='GPE':
        locations.append(loc[0])
###Places Mentioned in the text
print(set(locations))

print(blob.sentiment)


grammar = ('''NP: {<DT>?<JJ>*<NN>}''') # NP
chunkParser = nltk.RegexpParser(grammar)
tree = chunkParser.parse(tagged_sent)
tree.draw()
