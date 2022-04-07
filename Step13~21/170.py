num = []
num.append(int(input("first num : ")))
num.append(int(input("second num : ")))
num.sort()

while num[0] <= num[-1]:
    if num[0] % 5 == 0:
        print(num[0])
    num[0] += 1