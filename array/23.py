# Problem ID 23 Sort 0 1
def sort01(arr):
    size=len(arr)
    start=0
    end=size-1
    while(start<end):
        while(arr[start]==0 and start<end):
            start += 1
        while(arr[end]==1 and start<end):
            end -= 1
        if(start<end):
            temp=arr[start];
            arr[start]=arr[end]
            arr[end]=temp
            start += 1
            end -= 1

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
sort01(arr)
for number in arr:
    print(number,end=' ')
print()
