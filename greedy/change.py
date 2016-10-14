# Uses python3
import sys

def get_change(n):
    #print ("N is",n)
    number_of_coins = 0
    while n > 0:
        if n > 10:
            n = n - 10
            #print ("Adding 10s")
            number_of_coins += 1
        if n < 10 and n >= 5:
            n = n - 5
            #print ("Adding 5s")
            number_of_coins += 1
        if n < 5 and n >= 1:
            n = n - 1
            #print ("Adding 1s")
            number_of_coins += 1
    print (number_of_coins)
    return number_of_coins

def get_change_efficient(n):
    result = []
    denoms = [10, 5, 1]
    while n > 0:
        if n >= denoms[0]:
            num = n // denoms[0]
            n -= (num * denoms[0])
            result.append(num)
        denoms = denoms[1:]
    print (sum(result))
    return sum(result)

def main():
    n = int(input())
    if n < 1 or n > 10**3:
        return ""
    #print (get_change_efficient(n))
    return get_change_efficient(n)

if __name__ == '__main__':
    main()
