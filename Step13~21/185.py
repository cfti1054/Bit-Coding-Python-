num = int(input("Enter the number : "))
a = 1

while True:
    if num % 2 == 0:
        num = num / 2
        a += 1
    else:
        num = 2 * num + 2
        a += 1
    if num == 1:
        break
    

print(a)