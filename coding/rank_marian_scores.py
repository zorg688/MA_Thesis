import pandas as pd
import numpy as np

#read data

with open("../Sentence-level_Performance/cat+oci+spa-eng/scores_student1.decoded", mode ="r", encoding ="UTF-8") as file:
    decoded_scores = file.readlines()

with open("../Sentence-level_Performance/cat+oci+spa-eng/scores_student1.encoded", mode ="r", encoding ="UTF-8") as file:
    encoded_scores = file.readlines()

sorted_encoded = []
sorted_decoded = []

for data_ver, dataset in enumerate([decoded_scores, encoded_scores]):
    if data_ver == 0:
        for index, line in enumerate(dataset):
            sorted_decoded.append((f"Sentence{index+1}", float(line)))
    
        sorted_decoded = sorted(sorted_decoded, key=lambda x: x[1], reverse=True)
    else:
        for index, line in enumerate(dataset):
            sorted_encoded.append((f"Sentence{index+1}", float(line)))
    
        sorted_encoded = sorted(sorted_encoded, key= lambda x: x[1], reverse=True)

print("Top sentences based on decoded data:")
for i in range(5):
    print(sorted_decoded[i])

print("\nTop sentences bsed on encoded data: ")
for i in range(5):
    print(sorted_encoded[i])

#Save data as file
for index, dataset in enumerate([sorted_decoded, sorted_encoded]):
    df = pd.DataFrame(dataset)
    if index == 0:
        df.to_csv("../Sentence-level_Performance/cat+oci+spa-eng/student1_marian-scores_sorted.decoded", sep="\t", encoding="UTF-8", header=False, index=False)
    else:
        df.to_csv("../Sentence-level_Performance/cat+oci+spa-eng/student1_marian-scores_sorted.encoded", sep="\t", encoding="UTF-8", header=False, index=False)



