# Problem ID 29 Sort 0 1 2
def sort012(arr):
    n=len(arr)
    index2 = n - 1
    index0 = 0
    i = 0
    while(i<n and arr[i]==0):
        i += 1
    # Next zero will move to index0    
    index0 = i
    while(i <= index2):
        if(arr[i] == 0):
            temp = arr[index0]
            arr[index0] = arr[i]
            arr[i] = temp
            index0 += 1
        elif(arr[i] == 2):
            temp = arr[index2]
            arr[index2] = arr[i]
            arr[i] = temp
            index2 -= 1
            i -= 1
        i += 1

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
sort012(arr)
for number in arr:
    print(number, end=' ')
print()
