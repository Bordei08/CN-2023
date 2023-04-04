import numpy as np


e = 10 ** -9

# Aceste functie este folosita doar pentru a.txt, b.txt, aplusb.txt, ai.txt i = {1, 2, 3, 4, 5}.
def read_matrix(file_name):   
    file = open(f"res/{file_name}", "r")
    n = file.readline()
    n = int(n)

    a = [[] for i in range(n)]
    line = file.readline()
    while line:
        v = line.strip().split(",")
        v = [x.strip() for x in v]

        val = float(v[0])
        row = int(v[1])
        col = int(v[2])
        flag = False

        for x in a[row]:
            if x[1] == col:
                cx = x[0]
                a[row].remove(x)
                a[row].append((cx + val, col))
                flag = True
        if not flag:
            a[row].append((val,col))

        line = file.readline()
    file.close()
    return n, a

# Aceasta functie este doar pentru bi , i = {1, 2, 3, 4, 5}
def read_b(file_name):
    b = []
    file = open(f"res/{file_name}", "r")
    n = file.readline()

    line = file.readline()
    while line:

        b.append(float(line.strip()))
        line = file.readline()

    return n, b   

# verificam daca avem 0 pe diagonala
def get_matrix_check(n,a):
    for i in range(n):
        flag = False
        if len([x for x in a[i] if x[1] == i and abs(x[0]) > 10 ** -1]):
            flag = True
        if flag == False:
            raise SystemExit("Matricea are 0 pe diagonala", 1)
    return True


def gaus_seidel(n , a, b):

    x_gs = np.zeros(n)
    x_gs = np.array(x_gs)
    d_x = 1
    k = 0

    while d_x >= e and k < 10000:
        d_x = 0
        for i in range(n):
            s = 0
            for x in a[i]:
                if x[1] == i:
                    val = x[0]
                else:
                    index = x[1]
                    s = s + x[0] * x_gs[index]

            
            if abs(val) > 1e-10:
                d_x = d_x + ((b[i] - s) / val - x_gs[i])**2
            else:
                d_x = d_x + ((b[i] - s) - x_gs[i]*val)**2;
            x_gs[i] = (b[i] - s)/val

        d_x = np.sqrt(d_x)    
        k = k + 1
    
    if abs(d_x) <= e:
        return x_gs
    return "Error: Divergenta"    

def get_solution_check(a,x,b):
    result = [0 for i in range(len(b))]

    for i in range(len(a)):
        val = 0
        for y in a[i]:
            val = val + y[0] * x[y[1]]
        result[i] = val - b[i]

    err = 0
    for i in range(len(a)):
        aux = abs(result[i])
        if aux > err:
            err = aux

    return err        

               
                  
def use_case_1():
    n, a = read_matrix("a1.txt")
    m, b = read_b("b1.txt")

    if get_matrix_check(n,a):
        x = gaus_seidel(n, a, b)
        err = get_solution_check(a,x,b)
        return get_matrix_check(n,a),err
    else:
        return get_matrix_check(n,a),None   

def use_case_2():
    n, a = read_matrix("a2.txt")
    m, b = read_b("b2.txt")

    if get_matrix_check(n,a):
        x = gaus_seidel(n, a, b)
        err = get_solution_check(a,x,b)
        return get_matrix_check(n,a),err
    else:
        return get_matrix_check(n,a),None       

def use_case_3():
    n, a = read_matrix("a3.txt")
    m, b = read_b("b3.txt")

    if get_matrix_check(n,a):
        x = gaus_seidel(n, a, b)
        err = get_solution_check(a,x,b)
        return get_matrix_check(n,a),err
    else:
        return get_matrix_check(n,a),None   

def use_case_4():
    n, a = read_matrix("a4.txt")
    m, b = read_b("b4.txt")
    if get_matrix_check(n,a):
        x = gaus_seidel(n, a, b)
        err = get_solution_check(a,x,b)
        return get_matrix_check(n,a),err
    else:
        return get_matrix_check(n,a),None   

def use_case_5():
    n, a = read_matrix("a5.txt")
    m, b = read_b("b5.txt")
    if get_matrix_check(n,a):
        try:
            x = gaus_seidel(n, a, b)
            err = get_solution_check(a,x,b)
        except:
            err = None    
        return get_matrix_check(n,a),err
    else:
        return  get_matrix_check(n,a),None    




'''
use_case_1()
use_case_2()
use_case_3()
use_case_4()
use_case_5()

n , a = read_matrix("a5.txt")
m, b = read_b("b5.txt")
print(get_matrix_check(n, a))
x_s = gaus_seidel(n, a, b)
print(get_solution_check(a,x_s,b))
#print(get_equality(n,a,b))
##print(read_b("b1.txt"))
'''
#BONUS
#----------------------------------------------------------------
def check_result(a, b):
    n = len(a)
    m = len(b)
    for i in range(n):
        for x in a[i]:
            val1, col1 = x
            next_x = None
            for y in b[i]:
                if y[1] == col1:
                    next_x = y[0]
                    break
            if not next_x:
                return False
            val = next_x[0]
            if abs(val1- val2) >= e:
                return False

    return True     


def check_result_sum(m1, m2):
    n = len(m1)
    m= len(m2)
    for i in range(n):
        for x in m1[i]:
            val1, col1 = x
            y = next((x for x in m2[i] if x[1] == col1), None)
            if not y:
                return False
            val2 = y[0]
            if abs(val1 - val2) >= e:
                return False
    return True


def solve_bonus():
    n, a = read_matrix("a.txt")
    m, b  = read_matrix("b.txt")
    o, a_plus_b = read_matrix("aplusb.txt")
    sum = [[] for i in range(n)]

    for i in range(n):
        for x in a[i]:
            val_a, col_a = x
            val_b = next((y[0] for y in b[i] if y[1] == col_a), 0)
            if abs(val_a + val_b) > e:
                sum[i].append((val_a + val_b, col_a))

    for i in range(m):
        for y in b[i]:
            val_b, col_b = y
            val_a = next((x for x in a[i] if x[1] == col_b), None)
            if not val_a:
                sum[i].append((val_b, col_b))

    return check_result_sum(sum, a_plus_b)
    #print(check_result(sum, a_plus_b))

#solve_bonus()    