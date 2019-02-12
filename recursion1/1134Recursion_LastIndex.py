# Problem ID 1134 Last Index in Array 
def lastIndex(arr, x):
    size=len(arr)
    if size <= 0:
        return -1
    smallAns = lastIndex(arr[1:], x)
    if smallAns == -1:
        if x==arr[0]:
            return 0
        else:
            return -1
    else:
      return smallAns+1

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(lastIndex(arr, x))
