def equilibriumIndex(arr):
    n = len(arr)
    rightSum = 0
    leftSum = 0

    # Sum of all elements
    for i in range(n):
        rightSum += arr[i]

    for i in range(n):
        rightSum -= arr[i]
        if leftSum == rightSum:
            return i
        leftSum += arr[i]
    return -1

# Main
n = int(input())
arr = [int(i) for i in input().strip().split()]
print(equilibriumIndex(arr))
