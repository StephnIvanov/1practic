#-- coding: utf-8--

#b
import math

def number(x, y=None):
    if y is None:  
        y = 2

    if x <= 2:  
        return x == 2

    if y > math.isqrt(x): 
        return True if x > 1 else False  

    if x % y == 0:  
        return False
    return number(x, y + 1)  

z = int(input("Введите целое число больше 1: "))
if number(z):
    print("YES")
else:
    print("NO")
