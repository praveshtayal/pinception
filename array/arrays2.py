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
def sort012(int arr[], int n):
  int i,j,count[3]
  // Initialize count[i] to 0
  for(i=0; i<3; ++i)
    count[i]=0
  //Scan the input array
  for(i=0; i<n; ++i)
    count[arr[i]]++
  //Update the array
  for(i=0,j=0; j<count[0]; ++j)
    arr[i++] = 0
  for(j=0; j<count[1]; ++j)
    arr[i++] = 1
  for(j=0; j<count[2]; ++j)
    arr[i++] = 2

