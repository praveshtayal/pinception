# Problem ID 22 Sum of two Arrays
def sumOfTwoArrays(input1, input2):
    size1=len(input1)
    size2=len(input2)
    size3= size1 if size1>size2 else size2
    size3 += 1
    output = [0] * size3
    carry=0
    i1=size1-1
    i2=size2-1
    i3=size3-1
    while(i3>=0):
        sum = 0
        if(i1>=0):
            sum += input1[i1]
            i1 -= 1
        if(i2>=0):
            sum += input2[i2]
            i2 -= 1
        sum += carry
        carry = sum//10
        output[i3] = sum%10
        i3 -= 1
    return output

n1=int(input())
arr1=list(int(i) for i in input().strip().split(' '))
n2=int(input())
arr2=list(int(i) for i in input().strip().split(' '))
arr=sumOfTwoArrays(arr1, arr2)
for number in arr:
    print(number, end=' ')
print()
