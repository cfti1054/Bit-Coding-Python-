sum = 0

for i in range(1000000):
    if i % 2 == 0:
        sum -= i
    else:
        sum += i
    
    if sum >= 100:
        print(i)
        break