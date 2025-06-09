import numpy as np

import pandas as pd

with open("../Predictions_for_submission/Student_Predictions/defps-mul/defps-mul_transformer_model5.txt", mode= "r", encoding = "UTF-8") as file:
    text = file.readlines()


indexed_text = []

for index, line in enumerate(text):
    indexed_text.append((index+1, line))
sorted_text = sorted(indexed_text, key = lambda x: len(x[1]) )
print(sorted_text[0:10])



