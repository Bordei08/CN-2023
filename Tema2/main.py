import random

import numpy as np


def descompunerea_Choleski(A):
    n = len(A)
    L = np.zeros((n, n))
    D = [0.0] * n

    for p in range(n):

        L[p][p] = 1.0

        s = sum(D[k] * L[p][k] * L[p][k] for k in range(p))
        D[p] = A[p][p] - s

        for i in range(p, n):
            s = sum(D[k] * L[i][k] * L[p][k] for k in range(p))
            if abs(D[p]) < pow(10, -7):
                L[i][p] = (A[i][p] - s) / D[p]
            else:
                print("Nu se poate calcula solutia")
                break

    return L, D


def generate_matrix(n):
    A = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(i, n):
            if i == j:
                A[i, j] = random.randint(1, 10) * 10
            else:
                A[i, j] = A[j, i] = random.randint(-10, 10)
    A = np.dot(A, A.transpose())
    return A


def detA(L, D):
    det_L = np.linalg.det(L)

    det_D = 1
    for i in D:
        det_D *= i
    det_Lt = np.linalg.det(np.transpose(L))

    return det_L * det_D * det_Lt


def generate_b(n):
    return np.random.randint(100, 1000, n)


# cu diagonala 1
# matricea A este inferior triunghiulara, care de fapt e L
# e Ax=b dar pentru Lz=b
def Lz_b(L, b):
    n = len(L)
    z = [0.0] * n

    for i in range(n):
        s = sum([L[i][j] * z[j] for j in range(0, i)])
        z[i] = (b[i] - s)

    return z


def Dy_z(D, z):
    n = len(L)
    y = [0.0] * n

    for i in range(n):
        y[i] = z[i] / D[i]

    return y


def Ltx_y(Lt, y):
    n = len(Lt)
    x = [0.0] * n

    for i in reversed(range(0, n)):
        s = sum([Lt[i][j] * x[j] for j in range(i + 1, n)])
        x[i] = (y[i] - s)

    return x


def find_x(L, D, b):
    z = Lz_b(L, b)
    print("z = " + z.__str__())

    y = Dy_z(D, z)
    print("y = " + y.__str__())

    x = Ltx_y(np.transpose(L), y)
    print("x = " + x.__str__())

    return x


def descompunere_LU(A):
    L = np.linalg.cholesky(A)
    U = np.transpose(L)
    return L, U


def bonus(L, D, Ainit):
    LD = np.dot(L, np.diagflat(D))
    LDLt = np.dot(LD, np.transpose(L))

    rezultat = np.subtract(LDLt, Ainit)
    det_rezultat = np.linalg.det(rezultat)

    return det_rezultat


n = int(input("Introduceti dimensiunea matricii: "))
matrix = generate_matrix(n)
print(matrix)

print("*********************************")
print("L :")
L = descompunerea_Choleski(matrix)[0]
print(L)

print("*********************************")
print("D :")
D = descompunerea_Choleski(matrix)[1]
print(D)

print("*********************************")
print("Lt :")
print(np.transpose(L))

print("*********************************")
print("Verify difference:")

LD = np.dot(L, np.diagflat(D))
LDLt = np.dot(LD, np.transpose(L))
print(LDLt - matrix)

print("*********************************")
print("Det A:")
print(detA(L, D))

print("*********************************")
print("b :")
b = generate_b(n)
print(b)

print("*********************************")
print("Find x :")
x = find_x(L, D, b)

print("Verify: ")

print("Ax = ")
print(np.dot(matrix, x))
print("b =")
print(b)

print("*********************************")
print("Descompunerea LU a matricei A:")
L_LU, U_LU = descompunere_LU(matrix)
print(L_LU)
print(U_LU)
print(matrix)
print(np.dot(L_LU, U_LU))

print("*********************************")
'''
daca A = LU , Ax = b => Ly=b, Ux=y
'''
y_LU = Lz_b(L_LU, b)
x_LU = Ltx_y(U_LU, y_LU)
print("x = ")
print(x_LU)

print("*********************************")
print("Verify sol:")
eps = pow(10, -8)  # precizia
norma = np.linalg.norm((np.dot(matrix, x) - b), ord=2)
print(norma)
if norma < eps:
    print("Norma e buna")

print("*********************************")
print("BONUS")

eps = pow(10, -5)
corectitudinea_descompunerii = bonus(L, D, matrix)
print(corectitudinea_descompunerii)
if corectitudinea_descompunerii < eps:
    print("Corectitudinea e ok")
