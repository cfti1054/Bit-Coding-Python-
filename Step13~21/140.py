str1 = 'This is my best'
str2 = 'Do your best'

str1 = str1.split()
str2 = str2.split()

for i in str1:
    for j in str2:
        if i==j:
            print(i)

# str1 = set(str1.split(' '))
# str2 = set(str2.split(' '))
# print(str1.intersection(str2))