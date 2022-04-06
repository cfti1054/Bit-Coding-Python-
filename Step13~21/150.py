a = []
for i in ["x","y"]:
    a.append(int(input(f"{i}번째 좌표 입력 : ")))

if ((a[0] > 50) & (a[0] < 100)) & ((a[1] > 40) & (a[1] < 80)):
    print("사각형 안에 있습니다.")
else:
    print("사각형 안에 없습니다.")