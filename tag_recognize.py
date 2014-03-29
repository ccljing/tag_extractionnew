# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 14:35:33 2014

@author: jianglin02
"""
import nltk
import sys
import string
f = open("review","r")
valid =[]
def process():
    for line in f:
        text = nltk.word_tokenize(line)
        result = nltk.pos_tag(text)
        for i in range(0,len(result)):
            term = result[i][0]
            attr = result[i][1]
            if attr == "NN":
                valid.append(term)
    freq_dist = nltk.FreqDist(w.lower() for w in valid)
    print freq_dist.keys()[:10]
    
if __name__ == "__main__":
    process()
    
