a = 11
for i in range(a):
    for j in range(a*2-1):
        if i <= 5:
            if j in range(a-1-i, a+i):
                print('*', end ='')
            else:
                print(' ', end ='')
        else:
            if j in range(i, a*2-1-i):
                print('*', end = '')
            else:
                print(' ', end = '')
    print()