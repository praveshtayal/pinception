# Problem ID 25 Duplicate in Array
def MissingNumber(arr):
    size=len(arr)
    result = 0
    for i in range(0,size-1):
        result ^= i
        result ^= arr[i]
    return result^arr[size-1]

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
ans=MissingNumber(arr)
print(ans)
