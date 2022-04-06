import random

count = 0

for i in range(3):
    num = int(input(f"level{i+1} (1 ~ {2**(i+1)}) : "))
    if random.randrange(1, 2**(i+1)+1) == num:
        print("Correct!")
        count += 1
    else:
        print("Failure!")
        break

print(f"Answer is : {count}")