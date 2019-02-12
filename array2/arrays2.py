# Problem ID
def equilibrium(int arr[], int n):
    int f = 0
    int b = n-1

    if (n<3) return -1
    int sizef = arr[f]
    int sizeb = arr[b]
    while (b>2)
        sizeb += arr[--b]
    /* Here f=0, b=2 */
    int eq = 1
    for(eq=1; eq<n-2; eq++)
    
        if (sizef == sizeb) return eq
        sizef += arr[eq]
        sizeb -= arr[eq+1]
    return -1

# Problem ID
def PushZeroesEnd(int arr[], int n):
    int i, j
    for ( i=j=0; i<n; i++):
        if (arr[i] == 0) continue
        arr[j++] = arr[i]
    for ( ; j<n; j++):
        arr[j] = 0

# Problem ID
def Reverse(int arr[], int size):
    for(int i=0;i<size/2;++i):
    int temp = arr[i]
    arr[i] = arr[size-i-1]
    arr[size-i-1] = temp

# Problem ID
def Rotate(int arr[], int d, int size):
  d %= size
  Reverse(arr,size)
  Reverse(arr,size-d)
  Reverse(arr+size-d,d)

int FindSecondLargest(int arr[], int n):
  if(n <=1 ) return -2147483648
  int largest=arr[0], secondLargest=arr[1]
  if(largest<secondLargest)
    largest=arr[1]
    secondLargest=arr[0]
  for(int i=2; i<n; ++i):
    if(arr[i]>secondLargest)
      cout << "arr[i], largest, secondLargest are" <<
        arr[i] << " " << largest << ' ' << secondLargest << endl
      if(arr[i]>largest)
        secondLargest = largest
        largest = arr[i]
      else
        secondLargest = arr[i]
  return secondLargest

int FindSecondLargest2(int arr[], int n):
  if(n <=1 ) return -2147483648
  int largest=INT_MIN+1, secondLargest=INT_MIN
  for(int i=0; i<n; ++i)
    if(arr[i]>secondLargest)
      if(arr[i]>largest)
        secondLargest = largest
        largest = arr[i]
      else if(arr[i] != largest)
        secondLargest = arr[i]
  return secondLargest

int FindSortedArrayRotation(int arr[], int n):
  for(int i=1; i<n; ++i)
    if(arr[i-1]>arr[i])
      return i
    
  return 0

# Problem ID 29, sort012
def sort012(arr):
    n=len(arr)
    i0=0          # i0 is where 0 should go
    while i0<n and arr[i0]==0:
        i0 += 1
    # i0 now points to non 0 value
        
    i2=n-1        # i2 is where 2 should go
    while i2>i0 and arr[i2]==2:
        i2 -= 1
    # i2 now points to non 2 value
    i = i0        # we will move i from i0 to i2
    while i<=i2:
        # Skip 1
        if arr[i]==1:
            i += 1
        elif arr[i]==2:
            arr[i], arr[i2] = arr[i2], arr[i] # Swap values at i <-> i2
            i2 -= 1
        elif arr[i]==0:
            arr[i], arr[i0] = arr[i0], arr[i] # Swap values at i <-> i0
            i0 += 1
            i += 1

# Problem ID
def sumOfTwoArrays(int input1[], int size1, int input2[], int size2, int output[]):
  int i1,i2,i3,sum,carry=0
  int size3=(size1>size2?size1:size2)+1
  for(i1=size1-1, i2=size2-1, i3=size3-1; i3>=0; --i3)
    sum = 0
    if(i1>=0) sum += input1[i1--]
    if(i2>=0) sum += input2[i2--]
    sum += carry
    carry = sum/10
    output[i3] = sum%10

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
#SelectionSort(arr)
sort012(arr)
for number in arr:
    print(number, end=' ')
print()
