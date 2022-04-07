num = input("Enter the number : ")

sum = 0
for i in num:
    sum += int(i)

print(f"{num} 의 각 자리수의 합은 {sum}")