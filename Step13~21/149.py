# (1)
num1 = int(input("첫번째 숫자 입력 : "))
num2 = int(input("두번째 숫자 입력 : "))

if num1 <= num2:
    print(num2-num1)
else:
    print(num1-num2)

# (2)
Num = []

for i in range(3):
    Num.append(int(input(f"{i+1}번째숫자 입력 : ")))

Num.sort()
print(f"{Num[2]} * {Num[0]} - {Num[1]} = {Num[2]*Num[0]-Num[1]}")
