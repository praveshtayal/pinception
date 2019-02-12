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

def intersection(arr1, arr2):
    size1=len(arr1)
    size2=len(arr2)
    quickSort(arr1, 0, size1)
    quickSort(arr2, 0, size2)
    i=0
    j=0
    while(i<size1 and j<size2):
        if(arr1[i]==arr2[j]):
            print(arr1[i])
            i+=1
            j+=1
        elif arr1[i]<arr2[j]:
            i+=1
        else:
            j+=1


# Main
n1=int(input())
arr1=list(int(i) for i in input().strip().split(' '))
n2=int(input())
arr2=list(int(i) for i in input().strip().split(' '))
intersection(arr1, arr2) 
