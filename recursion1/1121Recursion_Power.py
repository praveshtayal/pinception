# Problem ID 1121 Power
def power(x, n):
    if n == 0:
        return 1
    smallAns = power(x,n-1)
    return smallAns * x

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
x, n=list(int(i) for i in input().strip().split(' '))
print(power(x, n))
