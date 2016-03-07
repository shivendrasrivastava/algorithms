# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

first_max = max(a)
a.remove(first_max)
second_max = max(a)
print (first_max * second_max)
