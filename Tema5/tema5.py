import numpy as np
import random

eps = 10 ** -9
kmax = 100000


def read_matrix(file_name):
    a_file = open(file_name, "r")
    dimension = int(a_file.readline())

    a = [[] for row in range(dimension)]
    while True:
        line = a_file.readline()

        if not line:
            break

        line = line.strip()

        values = line.split(",")
        values = list(map(lambda value: value.strip(), values))

        value = float(values[0])
        row = int(values[1])
        col = int(values[2])

        exists = False
        for elem in a[row]:
            if elem[1] == col:
                old_value = elem[0]
                a[row].remove(elem)
                a[row].append((old_value + value, col))
                exists = True
        if not exists:
            a[row].append((value, col))

    a_file.close()
    return a, dimension


# 1st point

a, dim = read_matrix("res/m_rar_sim_2023_512.txt")


# print(a)

def generateMatrix(n):
    randCount = random.randint(n, n * 10)
    a = [[] for i in range(0, n)]
    for i in range(0, randCount):
        value = random.random() * 10
        line = random.randint(0, n - 1)
        column = random.randint(0, n - 1)
        if len(a[line]) == 0:
            a[line].append((value, column))
            a[column].append((value, line))

    return a


def checkSym(a):
    n = len(a)
    for row in range(n):
        for (val, col) in a[row]:
            if not next(filter(lambda elem: abs(val - elem[0]) <= eps and elem[1] == row, a[col]), None):
                return False

    return True


a = generateMatrix(512)
print(checkSym(a))


# 2nd point

def matrixMultiplyVector(a, v):
    n = len(a)
    res = [0 for i in range(n)]

    for index in range(n):
        s = 0
        for elem in a[index]:
            col = elem[1]
            s += elem[0] * v[col]
        res[index] = s

    return res


def scalarMultiply(x, y):
    s = 0
    for i in range(len(x)):
        s += x[i] * y[i]
    return s


def euclidNorm(v):
    return np.sqrt(sum(map(lambda x: x * x, v)))


def powerMethod(a):
    n = len(a)
    x = np.random.randint(low=1, high=5, size=n)

    fractie = 1 / np.linalg.norm(x)
    v = [fractie * x[i] for i in range(n)]

    w = matrixMultiplyVector(a, v)
    lbd = scalarMultiply(w, v)
    k = 0

    # trece mereu prima data
    normToCheck = n * eps + 1

    while normToCheck > n * eps and k <= kmax:
        w_normal = euclidNorm(w)
        v = [w[i] / w_normal for i in range(n)]

        w = matrixMultiplyVector(a, v)
        lbd = scalarMultiply(w, v)
        k += 1
        normToCheck = euclidNorm(
            [(w[i] - lbd * v[i]) for i in range(n)]
        )

    if normToCheck > n * eps:
        raise ArithmeticError()

    return lbd, v

##################################################

a, dim = read_matrix("res/m_rar_sim_2023_512.txt")

if checkSym(a):
    l, v = powerMethod(a)
    print("Matricea e simetrica")
    print(l, v)
else:
    print("Matricea  nu e simetrica")

a, dim = read_matrix("res/m_rar_sim_2023_1024.txt")

if checkSym(a):
    l, v = powerMethod(a)
    print("Matricea e simetrica")
    print(l, v)
else:
    print("matricea  nu e simetrica")

a, dim = read_matrix("res/m_rar_sim_2023_2023.txt")

# if checkSym(a):
#     l, v = powerMethod(a)
#     print("Matricea e simetrica")
#     print(l, v)
# else:
#     print("matricea  nu e simetrica")
# print(dim)
#
# a = generateMatrix(512)
# if checkSym(a):
#     l, v = powerMethod(a)
#     print("Matricea e simetrica")
#     print(l, v)
# else:
#     print("matricea  nu e simetrica")

# 3rd point

# 1 valorile singulare ale matricei A

def singularValues(A):
    U, S, Vt = np.linalg.svd(A)

    print("Valorile singulare ale matricei A:")
    print(S)

    return S


# 2 rangul matricei A ( nr valori sing. > 0 )
def rang(A):
    U, S, V = np.linalg.svd(A)
    rang = 0
    for i in range(S.shape[0]):
        if S[i] > eps:
            rang += 1

    print("Rangul matricei A:")
    print(rang)

    return rang


# 3 numarul de conditionare al matricei A
# raportul dintre cea mai mare valoare singulara si cea mai mica valoare singulara strict pozitiva
def nrCond(A):

    U, S, V = np.linalg.svd(A)
    singMax = 0
    singMin = 0

    for i in range(S.shape[0]):
        if S[i] > eps:
            if S[i] > singMax:
                singMax = S[i]
            if S[i] < singMin or singMin == 0:
                singMin = S[i]

    nrCnd = singMax / singMin

    print("Numarul de conditionare al matricei A:")
    print(nrCnd)

    return nrCnd


# 4 pseudoinversa Moore-Penrose a matricei A, Ai apartine R^(nxp), Ai = VSUt
def pseudoInv(A):

    U, S, Vr = np.linalg.svd(A)

    singPositive = S[S > eps]

    Si = np.zeros((A.shape[1], A.shape[0]))

    for i in range(rang(A)):
        Si[i][i] = 1 / singPositive[i]

    Ai = np.dot(np.dot(Vr.T, Si), U.T)

    print("Pseudoinversa Moore-Penrose a matricei A")
    print(Ai)

    return Ai


# 5 vectorul xi
def xiNorm(A, b):
    Ai = pseudoInv(A)
    xi = np.dot(Ai, b)

    norm = np.linalg.norm(np.dot(A, xi) - b)
    print("Solutia sistemului Ax = b: ")
    print(xi)
    print("Norma:")
    print(norm)
    return xi, norm


# 6 calculati matricea pseudo-inversa in sensul celor mai mici patrate
def pseudoInvMatix(A):
    At = A.T

    print("Pseudoinversa Moore-Penrose in sensul celor mai mici patrate:")
    Aj = np.dot(np.linalg.inv(np.dot(At, A)), At)
    print(Aj)

    print("Norma:")
    norm = np.linalg.norm(pseudoInv(A) - Aj)
    print(norm)
    return Aj

def main():
    n = 4
    p = 4
    eps = 10 ** (-6)
    A = np.random.randint(20, size=(p, n))
    B = np.random.randint(20, size=p)
    singularValues(A)
    rang(A)
    nrCond(A)
    pseudoInv(A)
    xiNorm(A,B)
    pseudoInvMatix(A)

main()
