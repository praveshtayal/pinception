# Problem ID 1287 find unique
def uniqueElement(arr):
    size=len(arr)
    for i in range(0, size):
        for j in range(0, size):
            if(arr[i] == arr[j] and i!=j):
                break
        else:
            return arr[i]
    # Note that this return will never be excecuted but provided fro compiler
    # warning suppression.
    return arr[size-1]

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
number = uniqueElement(arr)
print(number)
