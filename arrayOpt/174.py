# Problem ID 174 Find Unique
def FindUnique(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
unique=FindUnique(arr)
print(unique)
