from math import sqrt
a = 2

def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
for i in range(3, 2000000, 2):
    if is_prime(i) == True:
         a += i
print(a)

