# Problem ID 1289 Array Intersection
def intersection(input1, input2):
    invalidBigNumber=999999999999999
    size1=len(input1)
    size2=len(input2)
    for i in range(0, size1):
        for j in range(0, size2):
            if(input1[i] == input2[j]):
                input2[j]=invalidBigNumber
                print(input1[i])
                break

n1=int(input())
arr1=list(int(i) for i in input().strip().split(' '))
n2=int(input())
arr2=list(int(i) for i in input().strip().split(' '))
intersection(arr1, arr2)
