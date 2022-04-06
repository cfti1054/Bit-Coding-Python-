number = int(input("정수입력 : "))

print("양수") if number < 0 else print("음수")
print("홀수") if number % 2 == 0 else print("짝수")
print("3의 배수") if number % 3 == 0 else print("3의 배수가 아님")
print("5의 배수") if number % 5 == 0 else print("5의 배수가 아님")
