#import numpy as np

#import pandas as pd

import os

def find_empty_preds():
    with open("../Predictions_for_submission/Student_Predictions/defps-mul/defps-mul_transformer_model5.txt", mode= "r", encoding = "UTF-8") as file:
        text = file.readlines()


    indexed_text = []

    for index, line in enumerate(text):
        indexed_text.append((index+1, line))
    sorted_text = sorted(indexed_text, key = lambda x: len(x[1]) )
    print(sorted_text[0:10])

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

if __name__ == "__main__":
    rename_preds()
