# Problem ID 28 Triplet Sum
def tripletSum(arr, x):
    size=len(arr)
    # Elements of list are in range 1 to 100
    elements = [0] * 101
    for num in arr:
        if 0<=num<=100:
            elements[num] += 1
    for i in range(1,(x//2)+1):
        product = 0
        if i==x-i:
            product = (elements[i]*(elements[i]-1))//2
        else:
            product = elements[i]*elements[x-i]
        for j in range(product):
            print(i, x-i)

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
sum=int(input())
tripletSum(arr, sum)
