import math

def ex1():
    exp = 1
    u = pow(10, -exp)
    while 1.0 + u != 1.0:
        exp = exp + 1
        u = pow(10,-exp)
    return u * 10  

print(ex1())      