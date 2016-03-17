#Uses python3
__author__ = "Shiven"

def lcm():
    n = input()
    numbers = n.split()
    least_common_multiple = 1
    if len(numbers) < 2:
        print ("Enter two numbers to calculate the LCM")
    n1 = int(numbers[0])
    n2 = int(numbers[1])
    least_common_multiple = (n1 * n2)//gcd(n1, n2)
    print (least_common_multiple)
    return least_common_multiple

def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

if __name__ == "__main__":
    lcm()
