from mlxtend.plotting import plot_confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

array_true =[]
array_predicted=[]


document_text = open("dict_final.txt", "r")
text_String = document_text.read().splitlines()
dictionary_model = {}
for word in text_String:
    # print("running1")
    word_tag = word.split("_")
    #print(word_tag)
    dictionary_model[word_tag[0]] = word_tag[1]


document_text = open("dict_given.txt", "r")

text_String = document_text.read().splitlines()
for word in text_String:
    # print("running2")
    word_tag = word.split("_")
    key = word_tag[0].lower()
    if key in dictionary_model:
    	array_true.append(word_tag[1]) 
    	array_predicted.append(dictionary_model[key])
    else:
    	array_true.append(word_tag[1])
    	array_predicted.append("NN1")
        
# print(array_true)
print(len(array_true))

# print(array_predicted)
class_names = ['NN1', 'VVB', 'CJC', 'PRP', 'AT0', 'NP0', 
'VBZ', 'POS', 'AJ0', 'CJS', 'VHZ', 'NN2', 'VBB', 
'VVN', 'AVP', 'PRF', 'VVZ', 'AV0', 'CRD', 'DTQ', 
'ORD', 'VBD', 'DPS', 'VVD', 'NN0', 'DT0', 'VHD', 
'VBG', 'PNP', 'VVG', 'TO0', 'VVI', 'VM0', 'VBI', 
'AJC', 'VHB', 'VBN', 'CJT', 'AJS', 'VDI', 'VDZ', 
'XX0', 'AVQ', 'EX0', 'VHI', 'VDD', 'UNC', 'PNI', 
'VDB', 'VDN', 'VHG', 'ZZ0', 'PNX', 'VHN', 'PUN', 
'PUL', 'PUR', 'PUQ', 'PNQ', 'ITJ', 'VDG']


# arr1 =["NN1"]
cf = confusion_matrix(array_true,array_predicted,class_names,normalize="pred")
precision = precision_score(array_true, array_predicted,labels=class_names, average='micro')
recall = recall_score(array_true, array_predicted,labels=class_names, average='micro')
score = f1_score(array_true, array_predicted,labels=class_names, average='micro')

print("values are")
print(precision)
print(recall)
print(score)

fig = plt.figure()

ax = fig.add_subplot(111)

# plot the matrix
cax = ax.matshow(cf,cmap="Blues")
# add colorbar for reference
fig.colorbar(cax)

ax.set_xticks(range(len(class_names)))
ax.set_yticks(range(len(class_names)))

ax.set_xticklabels(class_names)
ax.set_yticklabels(class_names)

plt.xticks(rotation=90)

# add labels to plot
plt.xlabel("Predicted")
plt.ylabel("True")
plt.savefig("Conf_Mat.jpg")
plt.show()