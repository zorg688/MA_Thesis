
def read_sentences(is_baseline, model_name, model_size, sentence_index):

    with open("data/4_Spanglish_Hinglish/mt_spanglisheng/test.txt", mode="r", encoding="UTF-8") as file:
        lines = file.readlines()
        sentence = lines[int(sentence_index)-1]
    print(f"This is the original sentence {sentence_index}:\n{sentence}\n")

    if not is_baseline:
        with open(f"../Predictions_for_submission/{model_name}_pred.en", mode="r", encoding="UTF-8") as file:
            lines = file.readlines()
            sentence = lines[int(sentence_index)-1]
        print(f"This is the teacher prediction for sentence{sentence_index}:\n{sentence}\n")

    if is_baseline:
        for index in range(5):
            with open(f"../Predictions_for_submission/Student_Predictions/{model_name}/{model_name}_{model_size}_model{index+1}.en", mode="r", encoding="UTF-8") as file:
                lines = file.readlines()
                print(f"Model {index+1} prediction for sentence {sentence_index}:\n{lines[int(sentence_index)-1]}\n")
    else: 
        for index in range(5):
            with open(f"../Predictions_for_submission/Student_Predictions/{model_name}/{model_name}_{model_size}_student{index+1}.en", mode="r", encoding="UTF-8") as file:
                lines = file.readlines()
                print(f"Model {index+1} prediction for sentence {sentence_index}:\n{lines[int(sentence_index)-1]}\n")


def check_baseline(model_index):
    return model_index in ["1", "2"]



if __name__=="__main__":
    model_sets = {"1": "baseline2021", 
                  "2": "baseline2023", 
                  "3": "cat+oci+spa-eng", 
                  "4": "mul-mul", 
                  "5": "defps-mul"}
    model_size = {"1": "transformer", "2": "transformer-tiny"}

    keep_going = True

    while True:
        print("These are the available models: ")
        for item in list(model_sets.items()):
            print(f"Press {item[0]} for model set {item[-1]}")
        print("Press 'c' to exit the selection")

        choice_model = input("\nEnter your choice here: ")

        if choice_model =="c":
            print("Goodbye!")
            break


        is_baseline = check_baseline(choice_model)

        print("\nThese are the possible model sizes: ")
        for item in list(model_size.items()):
            print(f"Press {item[0]} for model set {item[-1]}")
        choice_size = input("\nEnter your choice: ")

        print("\nThank you! Please choose a sentence index now")

        while True:
            sentence_index = input("Enter your index here: ")

            read_sentences(is_baseline, model_sets[choice_model], model_size[choice_size], sentence_index)

            input("\nWaiting for confirmation...")

            another_sentence = input("Would you like to check another sentence for the same set?\Press 'y' to choose another sentence, or press 'n' to go back to the set selection: ")

            if another_sentence =="n":
                break


