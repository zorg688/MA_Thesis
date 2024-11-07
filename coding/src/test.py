import os
import pandas as pd
import re


#read data
df = pd.read_csv("../data/DenglishCS/corpus_collapsed.csv")

#choose necessary columns
data = df[["sen_num", "token", "categ"]].values.tolist()

#collect tokens and build sentences
index = 1
line = []
sentences =[]
for sentence in data:
    if index == sentence[0]:
        line.append(sentence[1:])
    else:
        sentences.append(line)
        line = []
        line.append(sentence[1:])
        index = sentence[0]

#print(sentences[:30])

#check for code switching in sentences
d_count = 0
e_count = 0
de_en_sentences = []
en_de_sentences = []
for sentence in sentences:
    marks = [sent[-1] for sent in sentence]
    line = [sent[0] for sent in sentence]
    #print(marks)
    #print(line)
    d_count = marks.count("D")
    e_count = marks.count("E")

    if d_count > 0 and e_count > 0 and d_count > e_count:
        de_en_sentences.append(line)
    
    elif d_count > 0 and e_count > 0 and e_count > d_count:
        en_de_sentences.append(line)
    
    elif d_count > 0 and e_count > 0:
        de_en_sentences.append(line)
        en_de_sentences.append(line)

#save datasets
with open("../data/de_en.mixed", "w", encoding = "UTF-8") as file:
    for index, sentence in enumerate(de_en_sentences):
        if index == len(de_en_sentences)+1:
            file.write(" ".join(str(token) for token in sentence))
        else:
            file.write(" ".join(str(token) for token in sentence) + "\n")
        
    #sentences = ("\n").join(de_en_sentences)
    #file.writelines(sentences)

with open("../data/en_de.mixed", "w", encoding = "UTF-8") as file:
    for index, sentence in enumerate(en_de_sentences):
        if index == len(en_de_sentences)+1:
            file.write(" ".join(str(token) for token in sentence))
        else:
            file.write(" ".join(str(token) for token in sentence) + "\n")