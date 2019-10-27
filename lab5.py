import numpy as np
from math import sqrt
n = 3
A = []
eps = 0.00001

A = [[0]*n for i in range(n)]
B = n*[0]

A[0][0] = 1


def printMat():
    for i in range(0 , n):
        for j in range(0 , n):
            print(A[i][j],end=" ")
        print("")

def multMatByVec(mat ,vec):
    res = n  *[0]
    for i in range(n):
        for j in range(n):
            res += mat[i][j]*vec[j]
    return res

def vecSum(vec1 ,vec2):
    res = n * [0]
    for i in range(n):
        res = vec1[i] + vec2[i]
    return res

def simpleIterationsMethod():
    b = n * [0]
    for i in range(n):
        b[i] = B[i]/A[i][i]
    al = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            al[i][j] = A[i][j]/A[i][i]

    
    last = np.copy(B)

    while(True):
        xTemp = vecSum(B , multMatByVec(al,last))
        last = xTemp


def Zeidel(A, b):
    x = n * [0]

    converge = False
    while not converge:
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]

        converge = sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= eps
        x = x_new

    return x


def main():
    printMat()




if __name__ == "__main__":
    main()