import numpy as np

import pandas as pd

import gzip

with gzip.open("data/tc_Tatoeba-Challenge-v2021-08-07.source.gz", mode="r") as file:
    source_list = file.readlines()

print("loaded Source list!")
with gzip.open("data/tc_Tatoeba-Challenge-v2021-08-07.target.gz", mode="r") as file:
    target_list = file.readlines()
print("loaded Target list!")

removed_too_short = 0
removed_too_long = 0
removed_too_big_ratio = 0
removed_too_small_ratio = 0

length_small = 1
length_big = 150
ratio_small = 0.5
ratio_big = 2

length_before_filter = len(source_list)

for index in range(length_before_filter):
    source_sent = len(source_list[index].decode("UTF-8").strip("\n").split(" "))
    target_sent = len(target_list[index].decode("UTF-8").strip("\n").split(" "))

    if source_sent > length_big or target_sent > length_big:
        removed_too_long +=1
    elif source_sent < length_small or target_sent < length_small:
        removed_too_short +=1
    
    if source_sent / target_sent < ratio_small:
        removed_too_small_ratio +=1
    
    elif source_sent / target_sent > ratio_big:
        removed_too_big_ratio +=1

    print(f"Done with {np.round((index/length_before_filter)*100, 3)}%", end ="\r")

print("\nDone!")

print(f"Removed {removed_too_short} sentences because they were too short\nRemoved {removed_too_long} sentences because they were too long\nRemoved {removed_too_small_ratio} sentences because their ratio was too small\nRemoved {removed_too_big_ratio} sentences because their ratio was too big\nFinal dataset length: {length_before_filter-removed_too_big_ratio-removed_too_small_ratio-removed_too_short-removed_too_long}")


