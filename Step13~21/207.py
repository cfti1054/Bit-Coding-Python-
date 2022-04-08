from re import I


list = [5, 1, 7, 2, 6, 3]

def swap(i, j):
    a = i 
    i = j
    j = a

i, j = 3, 5
swap(i, j)
print(list)