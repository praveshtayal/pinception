# Problem ID 41 Digit Sum using recursion
def sumOfDigits(n):
    # Write a recursive function that returns the sum of the digits of a given
    # integer.
    if n == 0:
        return 0
    smallAns = sumOfDigits(n // 10)
    return smallAns + n%10

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
print(sumOfDigits(n))
