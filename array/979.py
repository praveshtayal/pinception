# Problem ID 979 Arrange Numbers in Array
def arrange(n):
    arr=[0] * n
    left=0
    right=n-1
    number=1
    while(left<right):
        arr[left] = number
        left += 1
        number += 1
        arr[right] = number
        right -= 1
        number += 1
    if(left==right):
        arr[left] = number
    return arr

n=int(input())
arr = arrange(n)
for number in arr:
    print(number, end=' ')
print()
