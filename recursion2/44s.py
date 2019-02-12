def mergeSort(arr, start, end):
    # Please add your code here
    pass

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr, 0, n)
print(*arr)
