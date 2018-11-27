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

import os
from wordcloud import WordCloud
import pysubs2
# import codecs 
import jieba
# import zmf
import matplotlib.pyplot as plt
#==============================================================================
# @zmf.tt

def is_chinese(uchar):         
    if '\u4e00' <= uchar<='\u9fff':
        return True
    else:
        return False
    
def wc(name, path):
    text =''
    for i in range(len(os.listdir(path))):
        try:
            f = pysubs2.load(path+ str(i+1) +'.ass',encoding='utf-8')
        except:
            try:
                f = pysubs2.load(path+ str(i+1) +'.ass',encoding='utf-16')
            except:
                continue
        for j in f:
            text += j.text
    #text = open(path.join(d, '../data/constitution.ass')).read()
    
    
      
    word_jieba = jieba.cut(text,cut_all=False)  
    word_split = ",".join(word_jieba)  
    
    word_list  = word_split.split(',')
    # trash1     = set(['be1','','fad','frz','pos','an7','fs18','Non','don','zipwinmax',
    #                   'fscx50','NT000A','Rcat'])
    trash2     = set(['好像','应该','可以','知道','不是','所以','没有','想要','什么',
                      '因为','就是','还是','这种','时候','但是','这样','这么','事情',
                      '的话','不过','觉得','真是','自己','那个','如果','虽然','不要',
                      '那么','不会','那样','哪里','那里','现在','就算','已经','这个',
                      '只是','只要','一个','而且','来说','只有','东西','这些','原来',
                      '怎么','似乎','可是','之后','一样','非常','而已','然后','完全',
                      '微软','雅黑','这里','我们','你们','他们','为了','这是','仪式',
                      '时间轴','翻译','特效','压制','淅沥','哗啦','片源','为什么','后期']) 
    # trash      = trash1 | trash2
    word_list  = list(filter(lambda a: a not in trash2, word_list))
    word_list  = list(filter(lambda a: is_chinese(a), word_list))
    word_split = ",".join(word_list)  
    
    # Generate a word cloud image
    wordcloud  = WordCloud(font_path='../data/simsun.ttc',width=1600, height=800).generate(word_split)
    
    # Display the generated image:
    # the matplotlib way:
    
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig(name+'.jpg', dpi = 600)
    
    # lower max_font_size
    #wordcloud = WordCloud(max_font_size=40).generate(text)
    #plt.figure()
    #plt.imshow(wordcloud)
    #plt.axis("off")
    #plt.show()
#==============================================================================
if __name__=='__main__':
    directory = '../data/ass/'
    names = os.listdir(directory)
    for name in names:
    #     try:
    #         wc(name,directory+name+'/','utf-8') #'utf-16-le' or 'utf-8'
    #     except:
    #         wc(name,directory+name+'/','utf-16')
    #     finally:
    #         print(name)
    # name = '幻想嘉年华'
        wc(name,directory+name+'/') #'utf-16-le' or 'utf-8'
#==============================================================================
