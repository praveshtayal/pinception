# Problem ID 981 Merge Sort
def merge(arr1, arr2):
    size1=len(arr1)
    size2=len(arr2)

    sizeM = size1+size2
    ans = [0] * (sizeM)
    i=0
    a1=0
    a2=0
    while(a1<size1 and a2<size2):
        if(arr1[a1]<=arr2[a2]):
            ans[i] = arr1[a1]
            a1 += 1
        else:
            ans[i] = arr2[a2]
            a2 += 1
        i += 1

    while(a1<size1):
        ans[i] = arr1[a1]
        a1 += 1
        i += 1

    while(a2<size2):
        ans[i] = arr2[a2]
        a2 += 1
        i += 1

    return ans

n1=int(input())
arr1=list(int(i) for i in input().strip().split(' '))
n2=int(input())
arr2=list(int(i) for i in input().strip().split(' '))
arr=merge(arr1, arr2)
for number in arr:
    print(number, end=' ')
print()
