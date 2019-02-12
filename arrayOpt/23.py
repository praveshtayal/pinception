# Problem ID 23 Sort 0 1
def SortZeroesAndOne(arr):
    n=len(arr)
    i=0
    j=n-1
    while(i<j):
        while(arr[i]==0 and i<n):
            i+=1
        while(arr[j]==1 and j>i):
            j-=1
        if(i<j):
            k=arr[i]
            arr[i] = arr[j]
            arr[j] = k
            i+=1
            j-=1

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
SortZeroesAndOne(arr, sum)
for num in arr:
    print(num, sep=' ')
print()
