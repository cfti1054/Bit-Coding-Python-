a = int(input('Enter the 1st number : '))
b = int(input('Enter the 2st number : '))

if a > b:
    c = a
    a = b
    b = c

sum = 0
for i in range(a, b):
    if a % 3 == 0:
        sum += a
    a += 1

print("a 부터 b까지의 합은 : ", sum)