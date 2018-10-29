# -*- coding: utf-8 -*-
"""
Created on Fri Sep  12 07:00:26 2018

@author: tejas
"""

# In[140]:


from bs4 import BeautifulSoup


# In[10]:


html=['<html><heading style="font-size:20px"><i>This is the title<br><br></i></heading>',
     '<body><b>This is the body</b><p id="para1">This is para1<a href="www.google.com">Google</a></p>',
     '<p id="para2">This is para 2</p></body></html>']


# In[141]:


import nltk
nltk.download('wordnet')


# In[12]:


html


# In[14]:


html=''.join(html)
print(html)
soup=BeautifulSoup(html, 'lxml')
print(soup.prettify())


# In[15]:


soup.html.name


# In[16]:


soup.body.text


# In[17]:


bold=soup.findAll('b')


# In[18]:


bold


# In[116]:


import urllib.request


# In[117]:


link = "https://qz.com/india/1367236/kerala-floods-show-how-climate-change-threatens-india/"


# In[118]:


req=urllib.request.Request(link)
response=urllib.request.urlopen(req)
the_page=response.read()


# In[119]:


the_page


# In[122]:


soup=BeautifulSoup(the_page, 'lxml')
paras=' '.join([p.text for p in soup.findAll('p')])
print(paras)


# In[123]:


sents = sent_tokenize(paras)
print(len(sents))


# In[124]:


words = word_tokenize(paras)
print(len(words))


# In[128]:


sents


# In[129]:


sents = sents[:-4]


# In[130]:


paras = "".join(sents)
paras


# In[103]:


from nltk.corpus import stopwords
from string import punctuation
custom = set(stopwords.words('english')+list(punctuation)+[',', '“', '’'])


# In[132]:


words=word_tokenize(paras)
print(len(words))


# In[134]:


words=[word for word in words if word not in custom]
print(len(words))


# In[106]:


print(words)


# In[147]:


words = [x.lower() for x in words]
words
from nltk.stem import WordNetLemmatizer
lmtzr = WordNetLemmatizer()
tokens = [lmtzr.lemmatize(word) for word in words]
preprocessed_text= ' '.join(tokens)
from collections import Counter
counts = Counter(words)
counts = counts.most_common()
print(counts)


# In[148]:


final_words_we_need = [x for x in counts if x[1]>3]
final_words_we_need

