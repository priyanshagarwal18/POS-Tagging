import os
import csv
import xml.etree.ElementTree as ET
from collections import defaultdict


document_text = open("dict_final.txt", "r")
text_String = document_text.read().splitlines()
dictionary_model = {}
for word in text_String:
    # print("running1")
    word_tag = word.split("_")
    print(word_tag)
    dictionary_model[word_tag[0]] = word_tag[1]


correct_outputs = 0
skipped = 0
print("came here")


# test data
total = 0
confusion_matrix = defaultdict(dict)

document_text = open("dict_given.txt", "r")
text_String = document_text.read().splitlines()
for word in text_String:
    # print("running2")
    word_tag = word.split("_")
    key = word_tag[0].lower()
    if key in dictionary_model:
        #constructiong confusion matrix
        try:
            confusion_matrix[word_tag[1]][dictionary_model[key]]+=1    
        except:
            confusion_matrix[word_tag[1]][dictionary_model[key]]=1     
        #calculating accuracy      
        if dictionary_model[key] == word_tag[1]:
            correct_outputs = correct_outputs + 1
    else:
        #constructiong confusion matrix
        try:
            confusion_matrix[word_tag[1]]["NN!"]+=1    
        except:
            confusion_matrix[word_tag[1]]["NN!"]=1 

        #calculating accuracy     
        if word_tag[1] == "NN1":  # smoothing
            correct_outputs += 1
    

print("correct are")
print(correct_outputs)

print("confusion matrix is")        
for key in confusion_matrix.keys():
    print("%s,%s\n" % (key,confusion_matrix[key]))
 
# print(len(confusion_matrix))     
# print("done")
