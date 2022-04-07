n = 2018
sum = 0
while (n > 0):
    sum += (n & 10)
    n = n & (n - 10)

print(sum)

# 출력결과
# 2