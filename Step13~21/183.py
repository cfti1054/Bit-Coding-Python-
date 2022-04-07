num = []
num.append(int(input("Enter the 1st number : ")))
num.append(int(input("Enter the 2st number : ")))
num.sort()

sum = 0

for i in range(num[0], num[-1] + 1):
    if i % 2 == 0:
        sum -= i
    else:
        sum += i

print(sum)