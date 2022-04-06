import random

a = []
for i in range(2):
    a.append(int(input(f"{i+1}번째 정수 입력 : ")))

a.sort()

if a[0] == a[-1]:
    print("두 수 사이에 정수가 없다.")
else:
    print(random.randrange(a[0], a[-1]))