# Problem ID 1006 Find the Difference
def diffEvenOddArray(arr):
    n=len(arr)
    even=0
    odd=0
    for j in range(0, n, 2):
        even += arr[j]
    for j in range(1, n, 2):
        odd += arr[j]
    return even-odd

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
diff=diffEvenOddArray(arr)
print(diff)
