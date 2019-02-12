# Problem ID 177 Binary Search(Recursive)
def binarySearchIndex(arr, start, end, val):
    if(start>end):
        return -1
    mid=(start+end)//2
    if(val == arr[mid]):
        return mid
    elif(val>arr[mid]):
        return binarySearchIndex(arr,mid+1,end,val)
    else:
        return binarySearchIndex(arr,start,mid-1,val)

def binarySearch(arr, val):
    n=len(arr)
    return binarySearchIndex(arr,0,n-1,val)

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
val=int(input())
index=binarySearch(arr, val)
print(index)
