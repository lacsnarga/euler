import numpy as np
import math

list1 = np.linspace(1, 100 , num = 100)

number2 = (sum(list1))**2
number1 = 0
for i in list1:
    number1 += i **2

print(number2- number1)