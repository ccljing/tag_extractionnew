import sys
import tag_extraction

def process_result(filename, score_dict_file):
    fd = open(filename, "r")
    for j in fd:
        line_list = j.rstrip().split("\t")
        phone_name = line_list[0]
        file_name = "./data/" + line_list[1]
        tag_extraction.process(phone_name, file_name, score_dict_file)

if __name__ == "__main__":
    process_result(sys.argv[1], sys.argv[2])
