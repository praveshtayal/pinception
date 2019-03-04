# Problem ID 187 Push Zeros to end
def PushZeroesEnd(arr):
    n=len(arr)
    j=0
    for i in range(0, n):
        if (arr[i] == 0):
            continue
        arr[j] = arr[i]
        j += 1
    while(j<n):
        arr[j] = 0
        j += 1

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
PushZeroesEnd(arr)
for number in arr:
    print(number, end=' ')
print()
