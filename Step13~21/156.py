str = input("Enter : ")
list = str.split(" ")

if '+' in list:
    print(f"{int(list[0])} + {int(list[-1])} = {int(list[0])+int(list[-1])}")
elif '-' in list:
    print(f"{int(list[0])} - {int(list[-1])} = {int(list[0])-int(list[-1])}")
elif '*' in list:
    print(f"{int(list[0])} * {int(list[-1])} = {int(list[0])*int(list[-1])}")
elif '/' in list:
    print(f"{int(list[0])} / {int(list[-1])} = {int(list[0])/int(list[-1])}")