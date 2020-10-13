
import os
import csv
import xml.etree.ElementTree as ET


document_text = open("./train_output.txt","r")
text_String = document_text.read().splitlines()
frequency = {}
for word in text_String:
        if word in frequency:
                frequency[word] = frequency[word]+1
        else:
                frequency[word] = 1

output_file  = open("./Train_frequency.txt","w")
for key in frequency.keys():
        output_file.write("%s : %s\n" %(key, frequency[key]))


document_text = open("./test_output.txt","r")
text_String = document_text.read().splitlines()
dictionary = {}
for word in text_String:
        if word in dictionary:
                dictionary[word] = dictionary[word]+1
        else:
                dictionary[word] = 1

output_file  = open("./Test_frequency.txt","w")
for key in dictionary.keys():
        output_file.write("%s : %s\n" %(key, dictionary[key]))

