import pandas as pd
import numpy as np

#This script finds the most distant sentences from the ranked cosine similarity scores

def find_sentences(model_set1, model_set2, model_size1, model_size2, scope):

    #read data
    data_set1 = pd.read_csv(f"../Sentence-level_Performance/{model_set1}/{model_set1}_{model_size1}_total_scores_sorted.tsv", sep="\t")
    print(data_set1)




if __name__=="__main__":
    model_sets = {"1": "baseline2021", 
                  "2": "baseline2023", 
                  "3": "cat+oci+spa-eng", 
                  "4": "mul-mul", 
                  "5": "defps-mul"}
    model_size = {"1": "transformer", "2": "transformer-tiny"}

    keep_going = True

    while keep_going:
        print("These are the available models: ")
        for item in list(model_sets.items()):
            print(f"Press {item[0]} for model set {item[-1]}")

        choice_model1 = input("\nEnter your choice here: ")
        print("\nChoose a second score set.")
        choice_model2 = input("\nEnter your choice here: ")

        print("Thank you!")
        

        print("\nThese are the possible model sizes: ")
        for item in list(model_size.items()):
            print(f"Press {item[0]} for model set {item[-1]}")
        choice_size1 = input("\nEnter your choice: ")
        print("\nChoose a second model size.")
        choice_size2 = input("\nEnter your choice here: ")

        print("\nThank you! Please choose how many sentences you wish to find.")
        scope = input("Enter your choice here: ")


        find_sentences(model_sets[choice_model1],model_sets[choice_model2], model_size[choice_size1], model_size[choice_size2], scope)

        input("\nWaiting for confirmation...")

        decision = input("Would you like to check another set or another sentence? \nPress 'y'to keep going, or press 'n' to close the program: " )

        if decision == "n":
            keep_going = False