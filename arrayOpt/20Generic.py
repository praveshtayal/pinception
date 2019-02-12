def pairSum(arr, x):
    size = len(arr)
    arr.sort()  # Sort the list
    start=0
    end=size-1
    while start<end:
        if arr[start]+arr[end]==x:
            product = 0
            if arr[start]==arr[end]:
                count = end-start+1
                product = count*(count-1)//2
                start = end # To ensure that while loop exits
            else:
                startCount=1
                endCount=1
                while start+1<end and arr[start+1]==arr[start]:
                    startCount+=1
                    start+=1
                while start<end-1 and arr[end-1]==arr[end]:
                    endCount += 1
                    end -= 1
                product = startCount*endCount
            for j in range(product):
                print(arr[start], arr[end])
            start += 1
            end -= 1
        elif arr[start]+arr[end]<x:
            start += 1
        else:
            end -= 1

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
sum=int(input())
pairSum(arr, sum)
