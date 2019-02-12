# Problem ID 977 Fibonacci Number
def checkMember(n):
    if(n==0 or n==1 or n==2):
      return True
    a=0
    b=1
    while(b<n):
        c=a+b
        a=b
        b=c
    if(b==n):
      return True
    return False

n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")
