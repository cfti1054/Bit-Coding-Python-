num = int(input("Enter the number : "))

a = True

for i in range(2, num):
    if num % i == 0:
        a = False
        break

if a == False:
    print(f"{num} is not prime number")
else:
    print(f"{num} is prime number")
