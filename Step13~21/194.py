num = int(input("Enter the positive number : "))
biggest_prime = 1

for i in range(1, num):
    a = True
    for j in range(2, i):
        if i % j == 0:
            a = False 

    if a:
        biggest_prime = i
    
print(f'biggest prime number under {num} is {biggest_prime}')