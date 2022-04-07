int = int(input(' 정수를 하나 입력하시오 : '))

sum = 0
for i in range(1, int + 1):
    sum += i
    i += 1

print(f'1 부터 {int}까지의 합은 {sum}')