num = int(input("숫자 입력 : "))

print("2 또는 3의 배수? ")
if (num % 2 ==0) | (num % 3 == 0):
    print(True)
else:
    print(False)