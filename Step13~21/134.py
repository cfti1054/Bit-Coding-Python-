a = 0b1101001
b = 0b1011111

print(bin(a&b), a&b)    # 73
print(bin(a^b), a^b)    # 54
print(bin(a|b), a|b)    # 127
print(bin((a+b)>>3<<2), (a+b)>>3<<2)    # 100
print(bin(~a), ~a)  # -106