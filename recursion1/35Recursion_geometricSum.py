# Problem ID 35 Geometric Sum using recursion
def geometricSum(k):
    if k == 0:
        return 1
    smallAns = geometricSum(k-1)
    return smallAns + 1/pow(2,k)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
print(geometricSum(n))
