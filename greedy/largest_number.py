#Uses python3
__author__ = "Shiven"

def largest(n):
    numbers = n.split()
    numbers = list(map(int, numbers))
    large = ""
    while len(numbers) > 0:
        num = max(numbers)
        numbers.remove(num)
        large += str(num)
    return int(large)

def main():
    n = input()
    return largest(n)

if __name__ == "__main__":
    main()
