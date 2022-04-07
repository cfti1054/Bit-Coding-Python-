a = 0

for i in range(24):
    for j in range(60):
        time = str(i) + str(j)
        if '3' in time:
            a += 1
print(a)