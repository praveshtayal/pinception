# Problem ID 1176 Print Numbers from 1 to n
def printR(n):
    if(n<=0):
        return
    printR(n-1)
    print(n, end=' ')

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
printR(n)
print()
