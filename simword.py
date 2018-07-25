# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:36:58 2018

@author: tedoreve
"""

from nltk.corpus import words
import difflib
from googletrans import Translator



word = 'like'  

dic  = words.words()
sim  = difflib.get_close_matches(word, dic, n = 100, cutoff = 0.85)    

translator   = Translator()
translations = translator.translate(sim,dest='zh-cn')

print('')
for translation in translations:
    print(translation.origin, ' -> ', translation.text)
print('')
print(sim)