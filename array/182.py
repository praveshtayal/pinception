# Problem ID 182 Linear Search
def linearSearch(arr, val):
    n=len(arr)
    for j in range(0,n):
        if(val==arr[j]):
            return j
    return -1

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
val=int(input())
index=linearSearch(arr, val)
print(index)
