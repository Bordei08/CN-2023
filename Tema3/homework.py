import numpy as np
from numpy import linalg
import copy

e = 10 ** -10


def  calc_b(a,s):
    
    b = [0 for x in range(len(s))]
    for i in range(len(s)):
        for j in range(len(s)):
            b[i] = b[i] + s[j] * a[i][j]
          
    return b


def des_householder(a,b):
    
    n = len(b)
    A = copy.deepcopy(a)
    B = copy.deepcopy(b)
# Q_negat = I_n
    q_negat = [[0 for i in range(n)]for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                q_negat[i][j] = 1
            else:
                q_negat[i][j] = 0    

    for r in range(n - 1):
# constructia matricei P_r - Constanta Beta si vectorul u
        sigma = 0 
        for i in range(r, n):
            sigma = sigma + A[i][r] **2

        if sigma <= e:
            break # r = r + 1  <-> P_r = I_n (A singulara)

# k = sqrt(sigma)
        k = np.sqrt(sigma)
        if A[r][r] >= e:
            k = -k

# Calculez beta       
        beta  = sigma - k*A[r][r]    

# Calculez vectorul u
        u = [0 for i in range(n)]
        for i in range(n):
            if i ==  r:
                u[i] = A[r][r] - k
            elif i > r:
                u[i] = A[i][r]
            else:
                u[i] = 0  
# A = P_r * A
# transformarea coloanelor j = r + 1, ..., n
        for j in range(r + 1, n):
# calculam y
            y = 0
            for i in range(r, n):
                y = y + u[i] * A[i][j]
            y = y / beta  

            for i in range(r,n):
                A[i][j] = A[i][j] - y*u[i]

# transformarea coloanei r a matricei A
        A[r][r] = k
        for i in range(r + 1, n):
            A[i][r] = 0
# b = P_r * b
# recalculam y
        y = 0
        for i in range(r, n):
            y = y + u[i]*B[i]
        y = y /beta   

        for i in range (r,n):
            B[i] =B[i] - B[i] - y*u[i] 

# Q_negat = P_r * Q_negat
        for j in range(n):
            y = 0  
            for i in range(r,n):
                y = y + u[i]*q_negat[i][j]
            y = y / beta    

            for i in range(r,n):
                q_negat[i][j] = q_negat[i][j] - y * u[i] 

    return q_negat, A        

def get_inv_householder(a):
    
    B = [0 for i in range(len(a[0]))]


    a_inv = [[0 for i in range(len(a[0]))]for i in range(len(a[0]))]

    q_t, r = des_householder(a,B)
    
    for j in range(len(a[0])):
        b_2 = [q_t[i][j] for i in range(len(a[0]))]

        
        col_res = solve_system_no_library(r,b_2)

        for i in range(len(a[0])):
            a_inv[i][j] = col_res[i]

    return a_inv

   

def solve_system_no_library(a,b):
# A * x = b  <=> Q*R*x = B <=> Q^t*Q*R*x = Q^T*b <=> R*X = b * Q^t

    q_t , r = des_householder(a,b)
    member_r = np.dot(q_t,b).tolist()
    member_l = r

    result_x = [0 for i in range(len(member_r))]

    for i in range(len(member_r) - 1, -1, -1):
        s = 0
        for j in range(i + 1, len(member_r)):
            s = s + member_l[i][j] * result_x[j]

        result_x[i] = (member_r[i] - s) / member_l[i][i]    

    return result_x



def solve_system_library(a,b):
    q, r = linalg.qr(a)
    q_t = np.transpose(q)
    
    return linalg.solve(r, np.dot(q_t, b))




def create_final_result(a, s):
    b = calc_b(a, s)
    prag = 10 ** -6
    flag = False

    final_result = ""
    final_result = "Instantele generate random sunt :  \n" + "A este : " + str(a) + "\n"+ "s este : " + str(s) + "\n" + "b este : " + str (b) + "\n"
#Ex3 -------------------------------------------------
    
    x_result_householder = np.array(solve_system_no_library(a,b))
    
    x_result_library = solve_system_library(a,b)

    final_result = final_result + "Solutia  sistemului cu Householder : " + str(x_result_householder)+ "\n" + "Solutia sistemului cu bibloteca : " + str(x_result_library) + "\n" 
    
    err_x = linalg.norm(x_result_library - x_result_householder)
    flag = err_x < prag

    final_result = final_result + "|| X_QR - X_householder||_2 = " + str(err_x) +  " < 10^-6  " + str(flag)+"\n"

#Ex4---------------------------------------------------
    err_1 = linalg.norm(np.dot(a,x_result_householder) - b)
    flag = err_1 < prag
    final_result = final_result + "||a*X_householder - b ||_2 = " + str(err_1) +  " < 10^-6  " + str(flag)+ "\n"

    err_2 = linalg.norm(np.dot(a,x_result_library) - b)
    flag = err_2 < prag
    final_result = final_result + "||a*x_QR - b||_2 = " + str(err_2) + " < 10^-6 "+ str(flag)  +"\n" 

    err_3 = linalg.norm(x_result_householder - s)/ linalg.norm(s)
    flag = err_3 < prag
    final_result = final_result + "||(X_householder - S)||_2 /  ||S||_2 = " + str(err_3) + " < 10^-6 "+ str(flag) + "\n"

    err_4 = linalg.norm(x_result_library - s) / linalg.norm(s)
    flag = err_4 < prag
    final_result = final_result + "||X_OR - S||_2 / ||S||_2" + str(err_4)+ " < 10^-6 "+ str(flag) + "\n"

#Ex5--------------------------------------------------
    
    a_inv_householder = get_inv_householder(a)

    a_inv_library = linalg.inv(a)

    err_inv = linalg.norm(a_inv_householder- a_inv_library)
    flag = err_inv < prag
    final_result = final_result + "||A^-1_householder - A^-1_bibl||_2 = " + str(err_inv) + " < 10^-6 "+ str(flag)+ "\n"

   
    return final_result


def get_instance(n, minim, maxim):
       return np.random.randint(minim,maxim,size = (n,n)).tolist(), np.random.randint(minim,maxim,size = n).tolist()

def main(n, minim, maxim):
    a, s = get_instance(n,minim,maxim) 
    with open("result.txt", "w") as f:
        f.write(create_final_result(a,s))     

#main(30, -10, 10)    