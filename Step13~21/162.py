import random

num_list = []
num = 0

for i in range(4):
    num_list.append(random.randrange(10, 21))
print(num_list)

for i in range(4):
    num += num_list[i]
print(num)

if num / 4 >= 15:
    print("Big")
else:
    print("Small")