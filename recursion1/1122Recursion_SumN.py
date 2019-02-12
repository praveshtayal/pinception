# Problem ID 1122 Sum of Natural Numbers
def sum(n):
    if n == 1:
        return 1
    smallAns = sum(n-1)
    return smallAns + n

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
print(sum(n))
