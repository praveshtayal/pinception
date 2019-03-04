# Problem ID 24 Bubble Sort
def bubbleSort(arr):
    n=len(arr)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
bubbleSort(arr)
print(*arr)
