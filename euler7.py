import sympy as sp
number = 3
index=2
while index < 10001:
    number += 2
    if sp.isprime(number) == True:
        index += 1

print(number)