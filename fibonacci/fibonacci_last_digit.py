#Uses python3
__author__ = "Shiven"

from itertools import islice

def main():
    n = int(input())
    print (fibonacci_last(n))
#    for k in islice(fibonacci_gen(n), n, n+1):
#        k %= 10
#        print (k)
#        return k

def fibonacci_last(n):
    if n == 0 or n == 1:
        return 1
    return (fibonacci_last(n-1) + fibonacci_last(n-2)) % 10

def fibonacci_gen(n):
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

if __name__ =="__main__":
    main()
