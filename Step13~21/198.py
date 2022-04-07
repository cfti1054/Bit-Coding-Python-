a = set()
for i in range(1, 100):
    for j in range(1, 100):
        for z in range(1, 100):
            if i + j + z == 100:
                a.update({i, j, z})

print(len(a))