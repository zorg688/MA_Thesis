import pandas as pd
import numpy as np

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