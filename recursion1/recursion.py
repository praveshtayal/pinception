# Problem ID
def sum(n):
    if(n == 1):
        return 1
    smallAns = sum(n-1)
    return smallAns + n

# Problem ID
def sumArray(arr):
    n=len(arr)
    if(n == 1):
        return arr[0]
    smallAns = sumArray(arr[:n-1])
    return smallAns + arr[n-1]

bool checkNumber(arr, x):
    size=len(arr)
    # Given an array of length N and an integer x, you need to find if x is
    # present in the array or not. Return true or false.
    if size == 1:
        return x==arr[0]
    bool smallAns = checkNumber(arr, size-1, x)
    return smallAns || (x==arr[size-1])


# Problem ID
def firstIndex(arr, x):
    size=len(arr)
    if size <= 0:
        return -1
    if x==arr[0]:
        return 0
    smallAns = firstIndex(arr[1:], x)
    if smallAns == -1:
      return -1
    else:
      return smallAns+1

# Problem ID
def lastIndex(arr, x):
    size=len(arr)
    if(size <= 0):
        return -1
    if(x==arr[size-1]):
        return size-1
    smallAns = lastIndex(arr[0:-1], x)
    if(smallAns == -1)
      return -1
    else
      return smallAns

# Problem ID
def allIndexes(arr, x):
    size=len(arr)
    if size <= 0:
        return []
    smallAns = allIndexes(arr[0:-1],x)
    if x==arr[size-1]:
        smallAns.append(size-1)
    return smallAns

# Problem ID
def multiplyNumbers(m, n):
    if m==0 or n==0:
        return 0
    if n>0:
        smallAns = multiplyNumbers(m,n-1)
        return smallAns + m
    else:
        smallAns = multiplyNumbers(m,n+1)
        return smallAns - m

# Problem ID
def countZeros(n):
    if n<0:
        n *= -1;  # Make n positive
    if n<10:
        if n == 0:
            return 1
        return 0
    smallAns = countZeros(n // 10)
    if n%10==0:
        smallAns += 1
    return smallAns

def geometricSum(k):
    if k == 0:
        return 1
    double smallAns = geometricSum(k-1)
    return smallAns + 1/pow(2,k)

def RcheckPalindrome(str):
    size=len(str)
    if size <= 1:
        return true
    if str[0]!=str[size-1]:
        return false
    return RcheckPalindrome(str[1:-1])

# Problem ID
def sumOfDigits(n):
    # Write a recursive function that returns the sum of the digits of a given
    # integer.
    if n == 0:
        return 0
    smallAns = sumOfDigits(n // 10)
    return smallAns + n%10

# Problem ID
def replacePi(str):
    # Given a string, compute recursively a new string where all appearances of
    # "pi" have been replaced by "3.14".
    if len(str) == 0:
        return str
    elif(str[0]!='p')
        replacePi(str+1)
    elif len(str)==1:
        return
    elif str[1]=='i':
        size
        # Calculate Size
        for(size=2;str[size]!='\0';size++)
        for(i=size+2;i>=4;i--)
            str[i] = str[i-2]
        str[0] = '3'
        str[1] = '.'
        str[2] = '1'
        str[3] = '4'
        replacePi(str+4)
    else:
        replacePi(str+1)

# Problem ID
def removeX(str):
    # Given a string, compute recursively a new string where all 'x' chars have
    # been removed.
    if len(str) == 0:
        return
    elif str[0]!='x':
      removeX(str+1)
    else:
      for(i=0;str[i]!='\0';i++)
        str[i] = str[i+1]
      str[i] = '\0'
      removeX(str)

# Problem ID
def stringToNumberNonRecuresive(str):
    # Write a recursive function to convert a given string into the number it
    # represents. That is str will be a numeric string that contains only
    # numbers, you need to convert the string into corresponding integer and
    # return the answer.
    i, number=0
    for(i=0;str[i]!='\0';i++):
        digit = str[i]-'0'
        number = (number*10) + digit
    return number

# Problem ID
def stringToNumber(str):
    # Write a recursive function to convert a given string into the number it
    # represents. That is str will be a numeric string that contains only
    # numbers, you need to convert the string into corresponding integer and
    # return the answer.
    if len(str) == 0:
      return 0
    smallAns = stringToNumber(str+1)
    power=1
    for(i=1;str[i]!='\0';i++)
        power *= 10
    digit = str[0]-'0'
    return digit*power + smallAns

# Problem ID
def pairStar(str):
    if len(str) == 0:
        return
    pairStar(str+1)
    if(str[0]==str[1]):
        size
        # Calculate Size
        for(size=2;str[size]!='\0';size++)
        for(i=size+1;i>=2;i--)
            str[i] = str[i-1]
        str[1] = '*'

# Problem ID 173 Tower of Hanoi
def towerOfHanoi(n, source, auxiliary, destination):
    if n == 0:
        return
    if n == 1:
        print(source, destination)
      return
    towerOfHanoi(n-1,source,destination,auxiliary)
    print(source, destination)
    towerOfHanoi(n-1,auxiliary,source,destination)
