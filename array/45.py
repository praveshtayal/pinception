# Problem ID 45 Binary Search
def BinarySearch(arr, val):
    n=len(arr)
    front=0
    back=n-1
    if(val < arr[front] or arr[back] < val):
        return -1
    while(front<=back):
        mid=(front+back)//2
        if(val == arr[mid]):
            return mid
        elif(val>arr[mid]):
            front = mid+1
        else:
            back = mid-1
    return -1

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
val=int(input())
index=BinarySearch(arr, val)
print(index)
