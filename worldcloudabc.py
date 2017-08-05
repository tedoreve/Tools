# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 15:22:11 2017

@author: tedoreve
"""

"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

from os import path
from wordcloud import WordCloud
import ass
import codecs 
import jieba

d = path.dirname(__file__)
# Read the whole text.

with codecs.open('../data/constitution.ass','r',encoding='utf-16-le') as f:
    doc = ass.parse(f)
#text = open(path.join(d, '../data/constitution.ass')).read()
text =''
for i in range(len(doc.events)):
    text += doc.events[i].text
    
word_jieba = jieba.cut(text[1000:3000],cut_all=True)  
word_split = " ".join(word_jieba)  
# Generate a word cloud image
wordcloud = WordCloud(font_path='../data/simsun.ttc').generate(word_split)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")

# lower max_font_size
#wordcloud = WordCloud(max_font_size=40).generate(text)
#plt.figure()
#plt.imshow(wordcloud)
#plt.axis("off")
#plt.show()

