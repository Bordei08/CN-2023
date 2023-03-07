import numpy as np

def split_matrix(m, n):
	row, col = int(n // 2), int(n // 2)
	return m[:row, :col], m[:row, col:], m[row:, :col], m[row:, col:]

def multiply_Strassen(A,B,n, n_min):
	if n == n_min:
		return np.matmul(A,B)

	A11, A12, A21, A22 = split_matrix(A,n)
	B11, B12, B21, B22 = split_matrix(B,n)

	P1 = multiply_Strassen(A11 + A22, B11 + B22, n/2, n_min)
	P2 = multiply_Strassen(A21 + A22, B11 ,n/2, n_min)
	P3 = multiply_Strassen(A11, B12 - B22, n/2, n_min)	
	P4 = multiply_Strassen(A22, B21 - B11, n/2, n_min)	
	P5 = multiply_Strassen(A11 + A12, B22, n/2, n_min)
	P6 = multiply_Strassen(A21- A11, B11 + B12, n/2, n_min)
	P7 = multiply_Strassen(A12 - A22, B21 + B22, n/2, n_min)

	C11 = P1 + P4 - P5 + P7
	C12 = P3 + P5		
	C21 = P2 + P4	
	C22 = P1 + P3 - P2 + P6

	C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

	return C

def next_power_of_two(n):
    power = 1 ## incepem de la 1
    while power < n:
        power <<= 1 ## muta bitul la stanga deci merge pe  puterile lui 2
    return power

def padding_matrix(m, max_dim):
    padding = ((0, max_dim - m.shape[0]), (0, max_dim - m.shape[1]))
    m = np.pad(m, padding, mode='constant', constant_values=0)
    return m

def ex3(A, B, n_min):
    nA, mA = A.shape
    nB, mB = B.shape
    n = max(nA,mA,nB,mB)
    n = next_power_of_two(n)
    if nA + mA != 2 * n:
        A = padding_matrix(A, n)
    if nB + mB != 2 * n:
        B = padding_matrix(B, n)
    ##print(A)
    ##print(B)
    return multiply_Strassen(A,B,n,n_min)


'''
x = np.array([[1,0,0,0], [0,1,0,0], [0,0,1,0],[0,0,0,1]])
y = np.array([[1,0,0,0], [0,1,0,0], [0,0,1,0],[0,0,0,1]])
Exemplu 
print(np.matmul(x,y))
print(multiply_Strassen(x,x,4,2))
ex3(x,y,2)
print("////////////////")
Exemplu pentru bonus
x = np.random.randint(10, size=(8, 4))
y = np.random.randint(10, size=(3, 4))
ex3(x,y,2)
'''