import pandas as pd
import numpy as np
from collections import Counter
from math import sqrt

def get_prediction_paths():
    #Get prediction set paths through a simple choice series

    baseline_or_student = { "1": "baseline", "2": "student"}
    baseline_year = {"1": "2021", "2": "2023"}
    student_teachers = {"1": "cat+oci+spa-eng", "2": "mul-mul", "3": "defps-mul"}
    model_sizes = {"1": "transformer", "2": "transformer-tiny"}

    #Get first model specification
    set_choice = input("Choose your first model set!\nAre you working with a baseline model, or a student model set? \nPress 1 for Baseline\nPress 2 for Student\nEnter your answer here: ")

    print("One moment...\n\n")

    if baseline_or_student[set_choice]== "baseline":
        chosen_set = baseline_or_student[set_choice]
        set_year = input("What year of data are you working with? \nPress 1 for 2021\nPress 2 for 2023\nEnter your answer here: ")
        print("One moment...\n\n")
        chosen_models = chosen_set+baseline_year[set_year]
    elif baseline_or_student[set_choice] == "student":
        chosen_set = baseline_or_student[set_choice]
        set_teacher = input("What teacher model are you working with?\nPress 1 for 'cat+oci+spa-eng'\nPress 2 for 'mul-mul'\nPress 3 for defps-mul\nEnter your answer here: ")
        print("One moment...\n\n")
        chosen_models = student_teachers[set_teacher]
    
    size_choice = input("What model size are you working with?\nPress 1 for transformer size\nPress 2 for transformer-tiny size\nEnter your answer here: ")
    print("One moment...\n\n")

    chosen_size = model_sizes[size_choice]

    print(f"Your first set is {chosen_models}_{chosen_size}!\nPlease choose your next model set!\n\n")

    #Get second model specification
    set_choice2 = input("Are you working with a baseline model, or a student model set? \nPress 1 for Baseline\nPress 2 for Student\nEnter your answer here: ")

    print("One moment...\n\n")

    if baseline_or_student[set_choice2]== "baseline":
        chosen_set2 = baseline_or_student[set_choice2]
        set_year2 = input("What year of data are you working with? \nPress 1 for 2021\nPress 2 for 2023\nEnter your answer here: ")
        print("One moment...\n\n")
        chosen_models2 = chosen_set2+baseline_year[set_year2]

    elif baseline_or_student[set_choice2] == "student":
        chosen_set2 = baseline_or_student[set_choice2]
        set_teacher2 = input("What teacher model are you working with?\nPress 1 for 'cat+oci+spa-eng'\nPress 2 for 'mul-mul'\nPress 3 for defps-mul\nEnter your answer here: ")
        print("One moment...\\n")
        chosen_models2 = student_teachers[set_teacher2]
    
    size_choice2 = input("What model size are you working with?\nPress 1 for transformer size\nPress 2 for transformer-tiny size\nEnter your answer here: ")
    print("One moment...\n\n")

    chosen_size2 = model_sizes[size_choice2]


    print(f"Your second model set is {chosen_models2}_{chosen_size2}!\nYou will compare these predictions to {chosen_models}_{chosen_size}!\nNow collecting the prediction paths...\n\n")

    #Get actual paths for each set
    if chosen_set == "student":
        set1_predictions = [f"../Predictions_for_submission/Student_Predictions/{chosen_models}/{chosen_models}_{chosen_size}_student1.en", 
                            f"../Predictions_for_submission/Student_Predictions/{chosen_models}/{chosen_models}_{chosen_size}_student2.en", 
                            f"../Predictions_for_submission/Student_Predictions/{chosen_models}/{chosen_models}_{chosen_size}_student3.en", 
                            f"../Predictions_for_submission/Student_Predictions/{chosen_models}/{chosen_models}_{chosen_size}_student4.en", 
                            f"../Predictions_for_submission/Student_Predictions/{chosen_models}/{chosen_models}_{chosen_size}_student5.en"] 
    else:
        set1_predictions = [f"../Predictions_for_submission/Student_Predictions/{chosen_models}/{chosen_models}_{chosen_size}_model1.en", 
                            f"../Predictions_for_submission/Student_Predictions/{chosen_models}/{chosen_models}_{chosen_size}_model2.en", 
                            f"../Predictions_for_submission/Student_Predictions/{chosen_models}/{chosen_models}_{chosen_size}_model3.en", 
                            f"../Predictions_for_submission/Student_Predictions/{chosen_models}/{chosen_models}_{chosen_size}_model4.en", 
                            f"../Predictions_for_submission/Student_Predictions/{chosen_models}/{chosen_models}_{chosen_size}_model5.en"]
    
    if chosen_set2 == "student":
        set2_predictions = [f"../Predictions_for_submission/Student_Predictions/{chosen_models2}/{chosen_models2}_{chosen_size2}_student1.en", 
                            f"../Predictions_for_submission/Student_Predictions/{chosen_models2}/{chosen_models2}_{chosen_size2}_student2.en", 
                            f"../Predictions_for_submission/Student_Predictions/{chosen_models2}/{chosen_models2}_{chosen_size2}_student3.en", 
                            f"../Predictions_for_submission/Student_Predictions/{chosen_models2}/{chosen_models2}_{chosen_size2}_student4.en", 
                            f"../Predictions_for_submission/Student_Predictions/{chosen_models2}/{chosen_models2}_{chosen_size2}_student5.en"] 
    else:
        set2_predictions = [f"../Predictions_for_submission/Student_Predictions/{chosen_models2}/{chosen_models2}_{chosen_size2}_model1.en", 
                            f"../Predictions_for_submission/Student_Predictions/{chosen_models2}/{chosen_models2}_{chosen_size2}_model2.en", 
                            f"../Predictions_for_submission/Student_Predictions/{chosen_models2}/{chosen_models2}_{chosen_size2}_model3.en", 
                            f"../Predictions_for_submission/Student_Predictions/{chosen_models2}/{chosen_models2}_{chosen_size2}_model4.en", 
                            f"../Predictions_for_submission/Student_Predictions/{chosen_models2}/{chosen_models2}_{chosen_size2}_model5.en"]
    
    print("Collected prediction set paths!")
    print("Collecting sentence predictions...")

    return set1_predictions, set2_predictions, [chosen_models, chosen_size], [chosen_models2, chosen_size2]


def get_top_and_bottom_ranked_sentences():

    #Get top and bottom 100 sentences for cat+oci+spa-eng and baseline2021, both transformer size
    top_ranks = 100

    student_dataset = "../Sentence-level_Performance/cat+oci+spa-eng/Student_Total_Scores_Sorted.csv"
    baseline_dataset = "../Sentence-level_Performance/Baseline2021/Baseline_Total_Scores_Sorted.csv"

    student_data = pd.read_csv(student_dataset, encoding = "UTF-8")
    baseline_data = pd.read_csv(baseline_dataset, encoding = "UTF-8")


    #print(f"This is the top 150 of sentences:\n {data.head(150)}\n")

    #print(f"This is the last 50 of sentences:\n {data.tail(50)}")

    student_data = student_data.rename(columns = {'Unnamed: 0':"sentence_num", "Scores":"score"})
    baseline_data = baseline_data.rename(columns = {'Unnamed: 0':"sentence_num", "Scores":"score"})



    top_100_student = student_data.head(top_ranks)
    top_100_baseline = baseline_data.head(top_ranks)

    bottom_100_student = student_data.tail(top_ranks)
    bottom_100_baseline = baseline_data.tail(top_ranks)

    common_top_sentences = []
    common_bottom_sentences = []

    for index, sentence_set in enumerate([top_100_student, bottom_100_student]):
        for sentence_id in sentence_set["sentence_num"].values:
            if index == 0:
                if sentence_id in top_100_baseline["sentence_num"].values:
                    common_top_sentences.append((sentence_id, f"Rank {np.where(sentence_set == sentence_id)[0][0]} in student set", f"Rank {np.where(top_100_baseline["sentence_num"].values == sentence_id)[0][0]} in baseline set" ))
            elif index == 1:
                if sentence_id in bottom_100_baseline["sentence_num"].values:
                    common_bottom_sentences.append((sentence_id, f"Rank {np.where(sentence_set == sentence_id)[0][0]} in student set", f"Rank {np.where(bottom_100_baseline["sentence_num"].values == sentence_id)[0][0]} in baseline set" ))

    #print(f"These are the commonly occurring top 100 sentences in terms of cosine similarity: {common_top_sentences}\n")
    #print(f"These are the commonly occurring bottom 100 sentences in terms of cosine similarity: {common_bottom_sentences}\n")

    common_sentences = [element[0] for element in common_top_sentences]+[element[0] for element in common_bottom_sentences]

    only_commons_student = student_data[student_data["sentence_num"].isin(common_sentences)]
    only_commons_baseline = baseline_data[baseline_data["sentence_num"].isin(common_sentences)]

    #print("Common Student sentences:\n", only_commons_student)

    #print("Common Baseline sentences:\n", only_commons_baseline)

    only_commons_student.to_csv("../Sentence-level_Performance/cat+oci+spa-eng/Common_top100_bottom100_sentences.tsv", sep = "\t")
    only_commons_baseline.to_csv("../Sentence-level_Performance/Baseline2021/Common_top100_bottom100_sentences.tsv", sep = "\t")

    #print(len(common_top_sentences))
    #print(len(common_bottom_sentences))
    #print(len(common_sentences))


    common_top = pd.DataFrame(common_top_sentences)
    common_bottom = pd.DataFrame(common_bottom_sentences)


    common_top.to_csv("../Sentence-level_Performance/common_top_100_sentences.tsv", sep = "\t", index = False)
    common_bottom.to_csv("../Sentence-level_Performance/common_bottom_100_sentences.tsv", sep ="\t", index = False)
    #print(common_top)
    #print(common_bottom)
    print("Done!")


def rank_student_predictions():

    #get prediction paths
    set1_predictions, set2_predictions, set1_name_size, set2_name_size = get_prediction_paths()
    

    set1_pred = []
    set2_pred = []

    preds = []

    for index, predictions in enumerate([set1_predictions, set2_predictions]):
        for prediction in predictions:
            with open(prediction, encoding = "UTF-8", mode = "r") as file:
                preds = file.readlines()
                for i, pred in enumerate(preds):
                    preds[i] = pred.strip("\n")

                if index == 0:
                    set1_pred.append(preds)
                else:
                    set2_pred.append(preds)
    
    print("Done collecting the predictions!")

    #calculate prediction similarity

    print("Calculating Cosine similarities...\n\n")
    set1_sentence_percentages = {}
    set1_total_percentages = {}
    set2_sentence_percentages = {}
    set2_total_percentages = {}
    num_comparisons = 0


    for sets, predictions in enumerate([set1_pred, set2_pred]): #student predictions or baseline predictions
        for index1, model1 in enumerate(predictions):
            for index2, model2 in enumerate(predictions): #individual models
                if index2 > index1:
                    num_comparisons += 1
                    for prediction_index in range(len(model1)):
                        vec1 = Counter(model1[prediction_index])
                        vec2 = Counter(model2[prediction_index])

                        # Calculating cosine similarity
                        dot_product = sum(vec1[ch] * vec2[ch] for ch in vec1)
                        magnitude1 = sqrt(sum(count ** 2 for count in vec1.values()))
                        magnitude2 = sqrt(sum(count ** 2 for count in vec2.values()))
                        res = dot_product / (magnitude1 * magnitude2)

                        if sets == 0:
                            if f"Sentence{prediction_index+1}" not in list(set1_sentence_percentages.keys()):
                                set1_sentence_percentages[f"Sentence{prediction_index+1}"] = [(f"model{index1+1}-model{index2+1}", res)]
                                set1_total_percentages[f"Sentence{prediction_index+1}"] = res

                            else:
                                set1_sentence_percentages[f"Sentence{prediction_index+1}"].append((f"model{index1+1}-model{index2+1}", res))
                                set1_total_percentages[f"Sentence{prediction_index+1}"] += res

                        else:
                            if f"Sentence{prediction_index+1}" not in list(set2_sentence_percentages.keys()):
                                set2_sentence_percentages[f"Sentence{prediction_index+1}"] = [(f"model{index1+1}-model{index2+1}", res)]
                                set2_total_percentages[f"Sentence{prediction_index+1}"] = res

                            else:
                                set2_sentence_percentages[f"Sentence{prediction_index+1}"].append((f"model{index1+1}-model{index2+1}", res))
                                set2_total_percentages[f"Sentence{prediction_index+1}"] += res

        print(f"Done with set {sets+1}, number of sentence comparisons: {num_comparisons}")
        num_comparisons = 0

    #calculate average cosine similarity
    for sets in [set1_total_percentages, set2_total_percentages]:
        for key, value in list(sets.items()):
            sets[key] = value/10

    #sort scores in descending order
    sorted_set1_total_similarity = sorted(set1_total_percentages.items(), key = lambda x: x[1], reverse = True)
    sorted_set2_total_similarity = sorted(set2_total_percentages.items(), key = lambda x: x[1], reverse = True)


    sorted_set1_total_similarity = dict(sorted_set1_total_similarity)
    sorted_set2_total_similarity = dict(sorted_set2_total_similarity)


    #Save scores and sorted scores
    print("Saving Scores and sorted scores...\n\n")
    total_scores = [sorted_set1_total_similarity, sorted_set2_total_similarity]
    sentence_scores = [set1_sentence_percentages, set2_sentence_percentages]

    for index, score_set in enumerate([total_scores, sentence_scores]):
        if index == 0:
            for index2, scores in enumerate(score_set):
                data = pd.DataFrame.from_dict(scores, orient = "index", columns = ["Scores"])
                if index2 == 0:
                    data.to_csv(f"../Sentence-level_Performance/{set1_name_size[0]}/{set1_name_size[0]}_{set1_name_size[-1]}_total_scores_sorted.tsv",sep = "\t",  encoding = "UTF-8")
                else:
                    data.to_csv(f"../Sentence-level_Performance/{set2_name_size[0]}/{set2_name_size[0]}_{set2_name_size[-1]}_total_scores_sorted.tsv",sep = "\t",  encoding = "UTF-8")
            
        else:
            for index2, scores in enumerate(score_set):
                data = pd.DataFrame.from_dict(scores, orient = "index")
                if index2 == 0:
                    data.to_csv(f"../Sentence-level_Performance/{set1_name_size[0]}/{set1_name_size[0]}_{set1_name_size[-1]}_sentence_scores.tsv",sep = "\t",  encoding = "UTF-8")
                else:
                    data.to_csv(f"../Sentence-level_Performance/{set2_name_size[0]}/{set2_name_size[0]}_{set2_name_size[-1]}_sentence_scores.tsv",sep = "\t",  encoding = "UTF-8")
    
    print("All done!")




if __name__=="__main__":

    mode = int(input("What would you like to do? \nPress 1 for finding the top and bottom 100 sentences\nPress 2 for ranking unsorted predictions based on their cosine similarity\nEnter your answer here: "))

    if mode == 1:
        get_top_and_bottom_ranked_sentences()
    
    elif mode == 2: 
        print("Starting...")
        rank_student_predictions()

