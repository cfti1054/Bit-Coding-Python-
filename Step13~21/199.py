list1 = [1, 3, 7, 4, 8, 2, 5, 4]
list2 = [2, 5, 1, 3, 7, 4]
sum = 0

for i in list1:
    list1.pop()
    i ^= 2
    print(i)
    for j in list2:
        list2.pop()
        sum += i * j
print(sum)


# # 출력 결과
# 3
# 1
# 5
# 6
# 41