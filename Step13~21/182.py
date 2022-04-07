number = input('Enter the nimber : ')
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
a = True
num = 0

for i in number:
    if not(i in numbers):
        if i == '.':
            num += 1
            if num == 2:
                a = False
                break
        else:
            a = False
            break

print(f"{number} is numbers? {a}")
