a = 0
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j}", end = '\t')
        a += 1
        if a == 5:
            print("\n")
    print("\n")
    a = 0