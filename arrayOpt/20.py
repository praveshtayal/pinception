# Problem ID 27 Print Array Intersection
def quickSort(arr, start, end):
    size=end-start
    if size<=1:
        return
    pivot=start # partion element is at index start
    count=start # Calculate No of elements in arr which are <= pivot element
    for i in range(start+1,end):
        if arr[i]<=arr[pivot]:
            count += 1

    #Move the pivot element to correct position        
    temp = arr[pivot]
    arr[pivot] = arr[count]
    arr[count] = temp
    pivot = count;

    # partition the array
    left=start
    right=end-1
    while left<pivot:
        while arr[left]<=arr[pivot] and left<pivot:
            left+=1
        if left>=pivot:
            break
        while arr[right]>arr[pivot]:
            right-=1
        temp=arr[left]
        arr[left]=arr[right]
        arr[right]=temp
        left += 1
        right -= 1
    quickSort(arr, start, pivot);
    quickSort(arr, pivot+1, end);

def pairSum(arr, x):
    # Elements of list are in range 1 to 100
    elements = [0] * 101
    for num in arr:
        if(0<=num and num<=100):
            elements[num] += 1
    for i in range(1,(x//2)+1):
        if(i==x-i):
            product = (elements[i]*(elements[i]-1))//2
        else:
            product = elements[i]*elements[x-i]
        for j in range(0, product):
            print(i, x-i, sep=' ')

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
sum=int(input())
pairSum(arr, sum)
