#Uses python3
__author__ = "Shiven"
import math
from itertools import islice

def fibonacci(n):
    fib =  int(round(((1 + math.sqrt(5))**n - (1 - math.sqrt(5))**n)/(2**n * math.sqrt(5))))
    print (fib)
    return fib

def main():
    n = int(input())
    for k in islice(fibonacci_gen(), n, n+1):
        print (k)
        return k
    #print (fibonacci_gen(n))

def fibonacci_recr(n):
    if n == 1 or n == 2:
        return 1
    return (long(fibonacci_recr(n-1)) + long(fibonacci_recr(n-2)))

def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        print (a)
        a, b = b, a+b

if __name__ == "__main__":
    main()
