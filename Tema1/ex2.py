import math
import random

def ex1():
    exp = 1
    u = pow(10, -exp)
    while 1.0 + u != 1.0:
        exp = exp + 1
        u = pow(10,-exp)
    return u * 10  

def ex2():
    print(verf_adunarea(1.0, ex1(), ex1()))
    print(verf_inmultirea())

def verf_adunarea(x, y,z):
    if (x + y) + z != x + (y + z):
        return f"Adunarea nu este asociativa \n{x}\n{y}\n{z}" 
    return f"Adunarea este asociativa pentru numerele \n{x}\n{y}\n{z}"    

def verf_inmultirea():
    while True:
        x, y, z = random.random(), random.random(), random.random()
        if (x * y) * z != x * (y * z):
            return f"Inmultirea nu este asociativa  \n{x}\n{y}\n{z}"  
            
    
ex2()        