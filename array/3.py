# Problem ID 3 Reverse Array
def reverseArray(arr):
    size=len(arr)
    for j in range(0, size//2):
        number = arr[j]
        arr[j] = arr[size-1-j]
        arr[size-1-j] = number

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
reverseArray(arr)
for number in arr:
    print(number, end=' ')
print()
