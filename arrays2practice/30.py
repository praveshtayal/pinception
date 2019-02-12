# Problem ID 30 Check array rotation
def FindSortedArrayRotation(arr):
    n=len(arr)
    for i in range(1, n):
        if(arr[i-1]>arr[i]):
            return i
    return 0

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
number=FindSortedArrayRotation(arr)
print(number)
