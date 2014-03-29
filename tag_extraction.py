#-*-encoding:gbk-*-
import sys
import nltk
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize
from nltk.tag import pos_tag

cellphone_attribute = ['screen','price', 'battery']

def filter_with_attribution():
    pass

def process():
    
    for s in sys.stdin:
        m = s.replace(",",".").replace("and", ".").replace("or",".").replace(":",".").split(".")
        for f in m:
            d = wordpunct_tokenize(f)
            for index, m in enumerate(d):
                pos_str = ""
                if m in cellphone_attribute:
                    before = index-5
                    if before < 0:
                        before = 0
                    end = index + 6
                    if end > len(d)-1:
                        end = len(d)-1
                    pos_result = pos_tag(d[before:end])
                    for pos_index, pos_sent in enumerate(pos_result):
                        if pos_sent[1].find("JJ") != -1:
                            if pos_index+ before < index:
                                print pos_sent, ' '.join(d[pos_index+before:index+1])
                            else:
                                print pos_sent, ' '.join(d[index:pos_index+before+1])

if __name__ == "__main__":
    process()
