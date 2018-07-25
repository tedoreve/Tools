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

from wordcloud import WordCloud
import ass
import codecs 
import jieba
import zmf
#==============================================================================
@zmf.tt
def wc():
    text =''
    
    for i in range(14):
        with codecs.open('../data/ass/kon/'+ str(i+1) +'.ass','r',encoding='utf-16-le') as f:
            doc = ass.parse(f)
            for j in range(len(doc.events)):
                text += doc.events[j].text 
    #text = open(path.join(d, '../data/constitution.ass')).read()
    
    
      
    word_jieba = jieba.cut(text,cut_all=False)  
    word_split = ",".join(word_jieba)  
    
    word_list  = word_split.split(',')
    trash1     = set(['be1','','fad','frz','pos','an7','fs18','Non','don','zipwinmax',
                      'fscx50','NT000A','Rcat'])
    trash2     = set(['好像','应该','可以','知道','不是','所以','没有','想要','什么',
                      '因为','就是','还是','这种','时候','但是','这样','这么','事情',
                      '的话','不过','觉得','真是','自己','那个','如果','虽然','不要',
                      '那么','不会','那样','哪里','那里','现在','就算','已经','这个',
                      '只是','只要','一个','而且','来说','只有','东西','这些','原来']) 
    trash      = trash1 | trash2
    word_list  = list(filter(lambda a: a not in trash, word_list))
    word_split = ",".join(word_list)  
    
    # Generate a word cloud image
    wordcloud  = WordCloud(font_path='../data/simsun.ttc',width=1600, height=800).generate(word_split)
    
    # Display the generated image:
    # the matplotlib way:
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud)
    plt.axis("off")
    #plt.savefig('sample.jpg', dpi = 600)
    
    # lower max_font_size
    #wordcloud = WordCloud(max_font_size=40).generate(text)
    #plt.figure()
    #plt.imshow(wordcloud)
    #plt.axis("off")
    #plt.show()
#==============================================================================
if __name__=='__main__':
    wc()
#==============================================================================
