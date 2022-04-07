sentence = input("Enter the sentence : ")

for i in range(0, len(sentence)):
    for j in range(0, i+1):
        print(sentence[j], end = " ")
    print()