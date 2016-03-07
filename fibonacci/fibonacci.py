__author__ = "Shiven"
import math

def fibonacci():
    n = int(input())
    fib =  int(round(((1 + math.sqrt(5))**n - (1 - math.sqrt(5))**n)/(2**n * math.sqrt(5))))
    print (fib)
    return fib

if __name__ == "__main__":
    fibonacci()
