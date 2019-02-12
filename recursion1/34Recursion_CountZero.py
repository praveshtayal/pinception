# Problem ID 34 Count Zeros using recursion
def countZeros(n):
    if n<0:
        n *= -1;  # Make n positive
    if n<10:
        if n == 0:
            return 1
        return 0
    smallAns = countZeros(n // 10)
    if n%10==0:
        smallAns += 1
    return smallAns

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
print(countZeros(n))
