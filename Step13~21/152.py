colors = ['red', 'orange', 'blue', 'green', 'white', 'black', 'dark blue', 'purple']

color = input("Enter the color : ")

if color in colors:
    print("sorry")
else:
    colors.append(color)
    print(colors)