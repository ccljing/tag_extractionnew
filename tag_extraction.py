#-*-encoding:gbk-*-
import sys
import nltk
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize
from nltk.tag import pos_tag
# atrrbute list, we can set for more attributes
cellphone_attribute = ['screen','price', 'battery', 'phone']

def filter_with_attribution():
    pass

def process(phone_name, comment_file, score_dict_file):
    try:
        # extract tags for comment files
        result = extract_tags(comment_file)
        # load score dict
        score_dict = load_score_dict(score_dict_file)
        # get the socre result
        score_result = get_score(result, score_dict)
        tmp_str = phone_name
        for m in score_result:
            tmp_str += "\t" + m + ":" + str(score_result[m])
        print tmp_str
    except Exception, e:
        sys.stderr.write("exception:info=%s" %(e))

def get_score(info_dict, score_dict):
    global cellphone_attribute
    score_result = {}
    for s in cellphone_attribute:
        if score_result.get(s, None) == None:
            score_result[s] = 5.0
    for s in info_dict:
        score = 0.0
        total_num = 0
        for f in info_dict[s]:
            if score_dict.get(s, None) != None and score_dict[s].get(f, None) != None:
                num = 0 
                for m in info_dict[s][f]:
                    num += info_dict[s][f][m]
                total_num += num
                score += score_dict[s][f] * num
        if total_num ==0:
            score = 5.0
        else:
            score = score * 1.0 / total_num
        
        score_result[s] = score
    return score_result

def load_score_dict(score_dict_file):
    score_dict = {}
    fd = open(score_dict_file, "r")
    for j in fd:
        line_list = j.rstrip().split(" ")
        score = int(line_list[0])
        attri = line_list[1]
        aj_word = line_list[2]
        if score_dict.get(attri, None) == None:
            score_dict[attri] = {}
        if score_dict[attri].get(aj_word, None) == None:
            score_dict[attri][aj_word] = score
    return score_dict

def extract_tags(comment_file):
    result = {} 
    
    fd = open(comment_file, "r")
    for s in fd:
        m = s.replace(",",".").replace("and", ".").replace("or",".").replace(":",".").split(".")
        for f in m:
            d = wordpunct_tokenize(f)
            for index, t in enumerate(d):
                pos_str = ""
                if t in cellphone_attribute:
                    before = index-10
                    if before < 0:
                        before = 0
                    end = index + 10
                    if end > len(d)-1:
                        end = len(d)-1
                    pos_result = pos_tag(d[before:end])
                    for pos_index, pos_sent in enumerate(pos_result):
                        seg_for_word = ""
                        adjust_word = ""
                        if pos_sent[1].find("JJ") != -1:
                            seg_for_word =  ' '.join(d[index:pos_index + before + 1])
                            adjust_word = pos_sent[0]
                            if pos_index+ before < index:
                                seg_for_word = ' '.join(d[pos_index+before:index+1])
                            add_into_dict(result, t, adjust_word, seg_for_word)
    return result

def add_into_dict(info_dict, attribute, adjust_word, seg_for_word):
    if info_dict.get(attribute, None) == None:
        info_dict[attribute] = {}
    if info_dict[attribute].get(adjust_word, None) == None:
        info_dict[attribute][adjust_word] = {}
        info_dict[attribute][adjust_word][seg_for_word] = \
            info_dict[attribute][adjust_word].get(seg_for_word,0) + 1

def print_dict(info_dict):
    for s in info_dict:
        for m in info_dict[s]:
            total_num = 0
            for f in info_dict[s][m]:
            #    total_num += info_dict[s][m][f]
                print s + "\t" + m + "\t" + f
if __name__ == "__main__":
    process(sys.argv[1], sys.argv[2], sys.argv[3])
