import numpy as np

import pandas as pd

from zipfile import ZipFile

import os

import statistics as stats

import re
from datetime import datetime
from datetime import timedelta

def find_empty_preds():

    models = ["baseline2021", "baseline2023"]

    for model in models:
        for model_num in range(5):
            with open(f"../Predictions_for_submission/Student_Predictions/{model}/{model}_transformer_tiny_model{model_num+1}.txt", mode= "r", encoding = "UTF-8") as file:
                text = file.readlines()
            indexed_text = []

            for index, line in enumerate(text):
                indexed_text.append((index+1, line))
            sorted_text = sorted(indexed_text, key = lambda x: len(x[1]) )
            print(f"Empty Sentence predictions for Model {model} {model_num+1}\n", sorted_text[0:10])


def rename_preds():
    files = ["baseline2021", "baseline2023", "cat+oci+spa-eng", "mul-mul", "defps-mul"]

    filepath = "../Predictions_for_submission/Student_Predictions"

    models = ["model1", "model2", "model3", "model4", "model5"]

    iterator = 0

    for fileset in files:
            iterator +=1
            for model in models:
                if os.path.exists(f"{filepath}/{fileset}/{fileset}_transformer_{model}.en"):
                    os.rename(f"{filepath}/{fileset}/{fileset}_transformer_{model}.en", f"{filepath}/{fileset}/{fileset}_transformer_{model}.txt")
            print(f"Done with {iterator} of 5", end="\r") 


def find_good_sentences():
    file_dir = "data/4_Spanglish_Hinglish/mt_spanglisheng/test.txt"

    scored_sentences = []

    with open(file_dir, mode ="r", encoding="UTF-8") as file:
          lines = file.readlines()

    for index, line in enumerate(lines): 
        print(f"Working on line {index +1} out of 6500...", end="\r")
        line = line.strip("\n").split(" ")
        max_score = len(line)
        score = len(line)
        for token in line:
            if not token.isalnum():
                score -= 1
        scored_sentences.append((index+1, line, np.round(score/max_score, 8)))

    sorted_sentences = sorted(scored_sentences, key= lambda x: x[2], reverse = True)

    with open("sentences_for_checking.txt", mode ="w", encoding = "UTF-8") as file:
        for element in sorted_sentences:
            file.write(str(element[0]) + "\t" + " ".join(element[1]) + "\t" + str(element[2]) +"\n")
    print("\nDone!")

def show_scored_sentences(ranked_bool):

    sentences = pd.read_csv("sentences_for_checking.txt", sep="\t", names =["SentenceID", "Sentence", "Score"])

    print(sentences.sort_values("SentenceID", axis = 0)[:55])



def calculate_time():
    times = input("Input sequence of times: ")
    times = [float(duration) for duration in times.split(",")]
    print(f"Median is {stats.median(times)}")



def find_duplicate_train_sentences():

    with open("../../train_set.source", mode ="r", encoding ="UTF-8") as file:
        lines = file.readlines()
    
    print(f"Full length: {len(lines)}")
    print(f"Deduplicated: {len(set(lines))}")

    length = 0
    for index, line in enumerate(set(lines)):
        if len(line.split(" ")) > 3 and len(line.split(" ")) < 100:
            length +=1
        print(f"Sentence: {index}", end ="\r")
    
    print(f"\nWith Length Filter: {length}")



def calculate_training_time():

    models = ("baseline2021", "baseline2023", "cat+oci+spa-eng", "mul-mul", "defps-mul")
    sizes = ("transformer", "transformer-tiny")

    for model in models:
        for size in sizes:
            
            for index in range(5):
                with open(f"data/Times/{model}_{size}_{index+1}.log", mode = "r", encoding = "UTF-8") as file:
                    training_times = []
                    for line in file:
                        if re.search(".*Training", line):
                            training_times.append(re.sub("].*", "", line).replace('[','').strip("\n"))
                starting_time = datetime.strptime(training_times[0], "%Y-%m-%d %H:%M:%S")
                end_time = datetime.strptime(training_times[1], "%Y-%m-%d %H:%M:%S")
                duration = end_time-starting_time
                if index == 0:
                    all_times = duration.total_seconds()
                else:
                    all_times= all_times +duration.total_seconds()
                
                print(f"Training time for {model}_{size}_{index+1}:")
                print( f"Training from {starting_time} until {end_time}")
                print(f"Training Duration: {duration}")

            print(f"Average training time: {timedelta(seconds =all_times/5)} \n")


            

    




        

if __name__ == "__main__":
    #rename_preds()
    #find_good_sentences()
    #show_scored_sentences(True)
    #find_empty_preds()
    #package_predictions()
    #calculate_time()
    #find_duplicate_train_sentences()
    calculate_training_time()
