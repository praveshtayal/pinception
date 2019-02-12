# Problem ID 181 Selection Sort
def SelectionSort(arr):
    n=len(arr)
    for i in range(0, n-1):
        min=i
        for j in range(i+1, n):
            if(arr[j]<arr[min]):
                min = j
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
SelectionSort(arr)
for number in arr:
    print(number, end=' ')
print()
