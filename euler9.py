from math import sqrt
for a in range(1000):
    for b in range(a, 1000):
        d = a + b + sqrt(a**2 + b**2)
        if d == 1000:
            print(sqrt(a**2 + b**2)*a*b)
            break