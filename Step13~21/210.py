def fun(n):
    sum = 0
    for i in range(n):
        sum += i % 5
    return sum


n = int(input("Enter the number : "))
print(f"fun{n}의 return 값은 {fun(n)}이다.")