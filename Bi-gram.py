# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 12:42:28 2018

@author: tejas
"""
from nltk.corpus import stopwords
from string import punctuation
from nltk.tokenize import word_tokenize, sent_tokenize

from nltk import ngrams
text_gram='Batman is a fictional superhero appearing in American comic books published by DC Comics.'
bigram = list(ngrams((x.lower() for x in word_tokenize(text_gram) if x not in list(punctuation)) , 2)) 
print(bigram)
len(bigram)





import nltk

word_data = "The best performance can bring in sky high success."
nltk_tokens = nltk.word_tokenize(word_data)  	

print(list(nltk.bigrams(nltk_tokens)))
