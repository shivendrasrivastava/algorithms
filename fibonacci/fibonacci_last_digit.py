#Uses python3
__author__ = "Shiven"

from itertools import islice

def main():
    n = int(input())
    for k in islice(fibonacci_gen(n), n, n+1):
        k %= 10
        print (k)
        return k

def fibonacci_gen(n):
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

if __name__ =="__main__":
    main()
