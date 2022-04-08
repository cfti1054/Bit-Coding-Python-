def gcd(n, m):
    for i in range(max(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            return i
    return 1

def lcm(n, m):
    i = max(n, m)
    while True:
        if i % n == 0 and i % m == 0:
            break
        i += 1
    return i

n = int(input("Enter thr number : "))
m = int(input("Enter thr number : "))
print(f"GCD of {n} and {m} is {gcd(n ,m)}")
print(f"LCM of {n} and {m} is {lcm(n ,m)}")