# Problem ID 977 Fibonacci Number
def isPerfectSquare( n):
    from math import sqrt
    s = int(sqrt(n))
    return s*s==n

def checkMember(n):
    # n is fibonacci number if and only if 5x^2+-4 is perfect square
    n *= 5*n
    return isPerfectSquare(n+4) or isPerfectSquare(n-4)

n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")
