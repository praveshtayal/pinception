# Problem ID 1135 All Index in Array 
def allIndexes(arr, x):
    size=len(arr)
    if size <= 0:
        return []
    smallAns = allIndexes(arr[:size-1], x)
    if x==arr[size-1]:
        smallAns.append(size-1)
    return smallAns

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
ans=allIndexes(arr, x)
for number in ans:
    print(number, end=' ')
print()
