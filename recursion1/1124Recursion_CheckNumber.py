# Problem ID 1124 Check Number in Array
def checkNumber(arr, x):
    size=len(arr)
    # Given an array of length N and an integer x, you need to find if x is
    # present in the array or not. Return true or false.
    if size == 1:
        return x==arr[0]
    smallAns = checkNumber(arr[:size-1], x)
    return smallAns or (x==arr[size-1])

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
