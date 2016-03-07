# Uses python3
import sys
ask = True
while ask:
    values = sys.stdin.read()
    tokens = values.split()
    a = int(tokens[0])
    b = int(tokens[1])
    if (a >= 0 and a <= 9) and (b >= 0 and b <= 9):
        ask = False
        print (a+b)
