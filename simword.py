# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:36:58 2018

@author: tedoreve
"""

from nltk.corpus import words
from nltk.corpus import wordnet
import difflib
from googletrans import Translator


#==============================================================================

def similar(word, n, cutoff):
    dic  = words.words()
    sim  = difflib.get_close_matches(word, dic, n = n, cutoff = cutoff)    
    
    translator   = Translator()
    translations = translator.translate(sim,dest='zh-cn')
    
    print('')
    for translation in translations:
        print(translation.origin, ' -> ', translation.text)
    print('')
    return sim
    
#==============================================================================

def meaning(sim):
    synonyms = []
    
    for syn in wordnet.synsets(word):
        for lm in syn.lemmas():
                 synonyms.append(lm.name())
    print (set(synonyms))
    
    antonyms = []
    
    for syn in wordnet.synsets(word):
        for lm in syn.lemmas():
            if lm.antonyms():
                antonyms.append(lm.antonyms()[0].name())
    
    print(set(antonyms))
    return '有空做个APP'
    
#==============================================================================
if __name__ == '__main__':
    word   = 'liable'  
    n      = 100          #upper limit number of similar words
    cutoff = 0.75         #larger value means less words
    sim    = similar(word, n, cutoff)
    app    = meaning(sim)