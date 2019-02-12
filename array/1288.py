# Problem ID 1288 find duplicate
def missingNumber(arr):
    size=len(arr)
    for i in range(0, size):
        for j in range(0, size):
            if(arr[i] == arr[j] and i!=j):
                return arr[i]
    return arr[0]

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
number = missingNumber(arr)
print(number)
