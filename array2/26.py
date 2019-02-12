# Problem ID 26 Insertion Sort
def InsertionSort(arr):
    n=len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if(arr[j-1]>arr[j]):
                arr[j], arr[j-1] = arr[j-1], arr[j]

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
InsertionSort(arr)
print(*arr)
