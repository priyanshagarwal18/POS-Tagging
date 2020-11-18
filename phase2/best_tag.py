import os
import xml.etree.ElementTree as ET

# output_path = "/home/mahakbansal/Downloads/AI project/output/output.txt"
# output_f = open(output_path, "w")
train_word_tag = {}
train_new = {}
for subdir, dir, file in os.walk(r"./Assignment-files/Train-corpus"):
    for file_name in file:
        
        file_path = subdir + os.sep + file_name
        tree = ET.parse(file_path)
        root = tree.getroot()
        for element in root.iter("w"):
            word = element.text.lower().rstrip()
            tag = element.attrib.get("c5")
            tag_list = tag.split("-")
            for tags in tag_list:
                try:
                    try:
                        train_word_tag[tags][word] += 1
                    except:
                        train_word_tag[tags][word] = 1
                except:
                    train_word_tag[tags] = {word: 1}
            train_new[word] = {}
            for tags in tag_list:
                if word in train_new:
                    try:
                        train_new[word][tags] += 1
                    except:
                        train_new[word][tags] = 1
                else:
                    train_new[word] = {tags: 1}

        for element in root.iter("mw"):
            if element.text != None:
                word = element.text.lower().rstrip()
            mw_list = ""
            tag = element.attrib.get("c5")
            for words in element.iter("w"):
                mw_list += words.text.lower().rstrip()
            tag_list = tag.split("-")    
            for tags in tag_list:
                try:
                    try:
                        train_word_tag[tags][mw_list] += 1
                    except:
                        train_word_tag[tags][mw_list] = 1
                except:
                    train_word_tag[tags] = {mw_list: 1}
            train_new[mw_list] = {}
            for tags in tag_list:
                if mw_list in train_new:
                    try:
                        train_new[mw_list][tags] += 1
                    except:
                        train_new[mw_list][tags] = 1
                else:
                    train_new[mw_list] = {tags: 1}


        for element in root.iter("c"):
            word = element.text.rstrip()
            tag = element.attrib.get("c5")
            tag_list = tag.split("-")
            
            for tags in tag_list:
                try:
                    try:
                        train_word_tag[tags][word] += 1
                    except:
                        train_word_tag[tags][word] = 1
                except:
                    train_word_tag[tags] = {word: 1}
            train_new[word] = {}
            for tags in tag_list:
                if word in train_new:
                    try:
                        train_new[word][tags] += 1
                    except:
                        train_new[word][tags] = 1
                else:
                    train_new[word] = {tags: 1}
            

print("dictionary is")
# print(train_word_tag)
train_count = {}
train_emission_prob = {}
prior_prob_tag = {}

for k in train_word_tag.keys():
    train_emission_prob[k] = {}
    count = sum(train_word_tag[k].values())
    train_count[k] = count

total_tag_count = sum(train_count.values())

for tag in train_count.keys():
    prior_prob_tag[tag] = train_count[tag] / total_tag_count

final_tag = {}
train_new_prob = {}
for k in train_new.keys():
    train_new_prob[k] = {}
    f_tag = ""
    for k2 in train_new[k].keys():
        train_new_prob[k][k2] = (train_new[k][k2] / train_count.get(k2)) * (
            prior_prob_tag.get(k2)
        )
        final = max(train_new_prob[k], key=train_new_prob[k].get)
    final_tag[k] = final

output_file = open("dict_final.txt", "w")
for key in final_tag.keys():
    output_file.write("%s_%s\n" % (key, final_tag[key]))
