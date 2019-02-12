# Problem ID 29, sort012
def sort012(arr):
    n=len(arr)
    i0=0          # i0 is where 0 should go
    while i0<n and arr[i0]==0:
        i0 += 1
    # i0 now points to non 0 value
        
    i2=n-1        # i2 is where 2 should go
    while i2>i0 and arr[i2]==2:
        i2 -= 1
    # i2 now points to non 2 value
    i = i0        # we will move i from i0 to i2
    while i<=i2:
        # Skip 1
        if arr[i]==1:
            i += 1
        elif arr[i]==2:
            arr[i], arr[i2] = arr[i2], arr[i] # Swap values at i <-> i2
            i2 -= 1
        elif arr[i]==0:
            arr[i], arr[i0] = arr[i0], arr[i] # Swap values at i <-> i0
            i0 += 1
            i += 1

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
sort012(arr)
for number in arr:
    print(number, end=' ')
print()
