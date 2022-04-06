a = []

for i in range(3):
    a.append(int(input(f"{i+1}번째 정수 입력 : ")))

a.sort()
print(a[0])
