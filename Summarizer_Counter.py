# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:30:02 2018

@author: tejas
"""

Text = "The Indian state of Kerala has been devastated by severe floods. More than 350 people have died, while more than a million have been evacuated to over 4,000 relief camps. Tens of thousands remain stranded. The crisis is a timely reminder that climate change is expected to increase the frequency and magnitude of severe flooding across the world. Although no single flood can be linked directly to climate change, basic physics attests to the fact that a warmer world and atmosphere will hold more water, which will result in more intense and extreme rainfall. The monsoon season usually brings heavy rains but this year Kerala has seen 42% more rain than would be expected, with more than 2,300mm of rain across the region since the beginning of June, and over 700mm in August alone. These are similar levels seen during Hurricane Harvey, that hit Houston in August 2017, when more than 1,500mm of rain fell during one storm. Tropical cyclones and hurricanes, such as Harvey, are expected to increase in strength by up to 10% with a 2℃ rise in global temperature. Under climate change the probability of such extreme rainfall is also predicted to grow by up to sixfold towards the end of the century. The rivers and drainage systems of Kerala have been unable to cope with such large volumes of water and this has resulted in flash flooding. Much of that water would normally be slowed down by trees or other natural obstacles. Yet over the past 40 years Kerala has lost nearly half its forest cover, an area of 9,000 km², just under the size of Greater London, while the state’s urban areas keep growing. This means that less rainfall is being intercepted, and more water is rapidly running into overflowing streams and rivers."
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