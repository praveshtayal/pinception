# Problem ID 702 Maximize the sum
def maxPathSum(ar1, ar2):
    m=len(ar1)
    n=len(ar2)
    max=0
    suma=0
    sumb=0
    i=0
    j=0
    while(i<m and j<n):
        if(ar1[i]==ar2[j]):
            max += suma if suma>sumb else sumb
            max += ar1[i]
            i+=1
            j+=1
            suma = sumb = 0
        elif(ar1[i]<ar2[j]):
            suma += ar1[i]
            i += 1
        else:
            sumb += ar2[j]
            j += 1
    while (i<m):
        suma += ar1[i]
        i += 1
    while (j<n):
        sumb += ar2[j]
        j += 1
    max += suma if suma>sumb else sumb
    return max

n1=int(input())
arr1=list(int(i) for i in input().strip().split(' '))
n2=int(input())
arr2=list(int(i) for i in input().strip().split(' '))
sum=maxPathSum(arr1, arr2)
print(sum)
