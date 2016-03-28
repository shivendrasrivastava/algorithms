#Uses python3
__author__ = "Shiven"

def matrix_multiply(A,B,m):
    return [ [ ( A[r][0]*B[0][c] + A[r][1]*B[1][c] ) % m for c in range(2) ] for r in range(2) ]

def matrix_power(A,n,m):
    if n==0: return [ [1%m,0], [0,1%m] ] # identity modulo m
    B = matrix_power(A,n//2,m)
    C = matrix_multiply(B,B,m)
    if n%2==1: C = matrix_multiply(C,A,m)
    return C

def modular_fibonacci():
    numbers = input()
    n, m = map(int, numbers.split())
    A = matrix_power( [ [0,1], [1,1] ], n, m )
    print (A[1][0])
    return A[1][0]

if __name__ == "__main__":
    modular_fibonacci()
