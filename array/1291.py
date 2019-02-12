# Problem ID 1291 Triplet Sum
def printOrder(a, b, c):
    if(a<=b and a<=c):
        if(b<c):
            print(a, b, c, sep=' ')
        else:
            print(a, c, b, sep=' ')
    elif(b<=a and b<=c):
        if(a<c):
            print(b, a, c, sep=' ')
        else:
            print(b, c, a, sep=' ')
    else:
        if(a<b):
            print(c, a, b, sep=' ')
        else:
            print(c, b, a, sep=' ')

def tripletSum(arr, x):
    size=len(arr)
    for i in range(0, size):
        for j in range(i+1, size):
            for k in range(j+1, size):
                if(arr[i]+arr[j]+arr[k]==x):
                    printOrder(arr[i], arr[j], arr[k])

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
tripletSum(arr, x)
