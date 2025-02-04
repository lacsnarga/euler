import numpy as np
import math
list1 = np.linspace(1.0 , 20.0, 20)
number = 1
stop = True
while not stop:
    diviser = 0
    for i in list1:
        if number % i == 0:
            diviser += 1
        else:
            break
    if diviser == 20:
        stop = True
    else:
        number += 1

number = 1
for i in range(1, 21):
    number = np.lcm(number , i)

print(number)
