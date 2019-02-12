# Problem ID 980 Swap Alternate
def swapAlternate(arr):
    size=len(arr)
    for j in range(0,size-1,2):
        number = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = number

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
swapAlternate(arr)
for number in arr:
    print(number, end=' ')
print()
