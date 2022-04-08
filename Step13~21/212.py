def change(num):
    a = str(num)[::-1]  # 문자열 [시작:끝:규칙] -> [::-1] => 리스트 맨뒤부터 확인하겠다.
    return a

n = int(input("Enter the number : "))
print(change(n))