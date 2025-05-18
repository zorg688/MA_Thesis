import numpy as np

import pandas as pd

with open("test_doc.txt", mode="r", encoding="UTF-8") as file:
    test_list = file.readlines()

test_frame = pd.read_csv("test_doc.txt", sep="\t")

print(test_list)
print(test_frame)
print(np.where(test_frame["Start"]=="Moin")[0][0])

for thing in test_frame["Sentence"]:
    print(thing)