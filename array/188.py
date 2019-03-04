def Reverse(arr, start, end):
    while(start<end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def Rotate(arr, d):
    size=len(arr)
    d %= size
    Reverse(arr, 0, size-1)
    Reverse(arr, 0, size-d-1)
    Reverse(arr, size-d, size-1)

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
d=int(input())
Rotate(arr, d)
print(*arr)
