# Problem ID 1175 Count Digits
def count(n):
    if n == 0:
        return 0
    smallAns = count(n//10)
    return smallAns + 1

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
print(count(n))
