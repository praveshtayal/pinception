def mergeSort(input[], size):
    result[THOUSAND]
    if(size <= 1)
        return
    size1 = size/2
    size2 = size-size1
    mergeSort(input,size1)
    mergeSort(input+size1,size2)
    i=0, j=size1,k=0, temp
    while(i<size1 && j<size):
        if(input[i]<input[j])
            result[k++] = input[i++]
        else
            result[k++] = input[j++]
    while(i<size1)
            result[k++] = input[i++]
    while(j<size)
            result[k++] = input[j++]
    for i in range(0, n):(i=0;i<size;i++)
        input[i]=result[i]

def swap(input[], i, j):
    temp = input[i]
    input[i]= input[j]
    input[j] = temp

def quickSort(input[], size):
    if(input==nullptr || size<=1) return
    // size is atleast 2. 
    // Count no of elements smaller than input[0]
    count=0
    for i in range(0, n):(i=1; i<size; i++)
        if(input[i]<input[0])
            count++
    // count may be zero as well
    swap(input, 0, count)
    left=0, right=size-1
    while(left<count && right>count):
        while(input[left]<input[count]) left++
        while(input[right]>=input[count]) right--
        if(left<right)
            swap(input, left++, right--)
    quickSort(input, count)
    quickSort(input+count+1, size-count-1)

# Problem ID 1137, replaceCharacter
def replaceCharacter(string, c1, c2):
    if len(string)==0:
        return string
    string2 = replaceCharacter(string[1:],c1,c2)
    if string[0]==c1:
        return c2 + string2
    else:
        return c1 + string2

# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(string):
    if len(string)<=1:
        return string
    string2 = removeConsecutiveDuplicates(string[1:])
    if string[0]==string[1]:
        return string2
    else:
        return string[0]+string2

def subsequence(string input, string output[]):
    if(input.size()==0):
        output[0] = ""
        return 1

    ans = subsequence(input.substr(1), output)

    # copy the output
    for i in range(0, n):(i=0; i<ans; i++):
        output[ans+i] = input[0] + output[i]
    return ans*2

def printSubsequence(string prefix, string input):
    if(input.size()==0):
        print(prefix)
        return

    printSubsequence(prefix, input.substr(1))
    printSubsequence(prefix+input[0], input.substr(1))

def printSubsequence(string input):
    printSubsequence("", input)
