import numpy as np

#calculate size of Denglish dataset

def denglish():

    with open("../data/3_Denglish/de_en.mixed", "r", encoding = "UTF-8") as file:
        de_en_sent = file.read()
    de_en_sent = de_en_sent.split("\n")

    with open("../data/3_Denglish/en_de.mixed", "r", encoding = "UTF-8") as file:
        en_de_sent = file.read()
    en_de_sent = en_de_sent.split("\n")

    with open("../data/3_Denglish/denglish.mixed", "r", encoding = "UTF-8") as file:
        den = file.read()
    den = den.split("\n")
    print(f"Total size of Denglish Dataset: {len(den)} sentences")


#calculate spize of Spanglish dataset
def spanglish():

    with open("../data/4_Spanglish_Hinglish/mt_spanglisheng/spanglish.txt", "r", encoding = "UTF-8") as fileA, open("../data/4_Spanglish_Hinglish/mt_spanglisheng/test.txt", "r", encoding = "UTF-8") as fileB:
        spang_sent = fileA.read()
        test_sent = fileB.read()
    
    spang_sent = spang_sent.split("\n")
    test_sent = test_sent.split("\n")
    
    spang_data = spang_sent + test_sent

    

    print(f"Training set size of Spanglish Dataset: {len(spang_sent)} sentences")
    print(f"Test set size of Spanglish Dataset: {len(test_sent)} sentences")
    print(f"Total size of Spanglish Dataset: {len(spang_data)} sentences")
    

 # calculate size of Hinglish datasets   
def hinglish():

    #dataset 1
    with open("../data/8_Hinglish/s-enhi.txt", "r", encoding = "UTF-8") as file:
        hing_sent = file.read()
    hing_sent = hing_sent.split("\n")
    print(f"Total size of first (natural) Hinglish Dataset: {len(hing_sent)} sentences")
    print()

    #dataset 2
    with open("../data/9_Hinglish/all.txt", "r", encoding = "UTF-8") as fileA, open("../data/9_Hinglish/test.txt", "r", encoding = "UTF-8") as fileB, open("../data/9_Hinglish/train.txt", "r", encoding = "UTF-8") as fileC, open("../data/9_Hinglish/validation.txt", "r", encoding = "UTF-8") as fileD:
        hing_all_sent = fileA.read()
        hing_test_sent = fileB.read()
        hing_train_sent = fileC.read()
        hing_val_sent = fileD.read()

    hing_all_sent = hing_all_sent.split("\n\n")
    hing_test_sent = hing_test_sent.split("\n\n")
    hing_train_sent = hing_train_sent.split("\n\n")
    hing_val_sent = hing_val_sent.split("\n\n")
    
    print(f"Training set size of second (synthetic) Hinglish Dataset: {len(hing_train_sent)} sentences")
    print(f"Test set size of second (synthetic) Hinglish Dataset: {len(hing_test_sent)} sentences")
    print(f"Validation set size of second (synthetic) Hinglish Dataset: {len(hing_val_sent)} sentences")
    print(f"Total size of second (synthetic) Hinglish Dataset: {len(hing_all_sent)} sentences")


print("SIZES OF DATASETS")
denglish()
print()
spanglish()
print()
hinglish()
