#Uses python3
__author__ = "Shiven"

def gcd():
    n = input()
    numbers = n.split()
    dividend = 0
    divisor = 0
    if len(numbers) < 2:
        print ("Enter two numbers to calculate GCD ")
    if int(numbers[0]) > int(numbers[1]):
        dividend, divisor = int(numbers[0]), int(numbers[1])
    else:
        dividend, divisor = int(numbers[1]), int(numbers[0])
    quotient = 1
    while quotient > 0:
        quotient = dividend % divisor
        dividend, divisor = divisor, quotient
    print (dividend)
    return dividend

if __name__ == "__main__":
    gcd()
