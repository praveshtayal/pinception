# Probelm ID 532, shortestSubsequence
def shortestSubsequence(s, v):
    if len(s)==0:
        return None
    index = v.find(s[0])
    if index==-1:
        return s[0]
    op1 = shortestSubsequence(s[1:], v)
    op2 = shortestSubsequence(s[1:], v[index+1:])
    if op2 is None:
        op2 = s[0]
    else:
        op2 = s[0] + op2
    if op1 is None:
        return op2
    # Both op1 and op2 exist
    if len(op1)<len(op2):
        return op1
    else:
        return op2

# Main
s=input().strip()
v=input().strip()
ans=shortestSubsequence(s,v)
print(ans)
print(len(ans))
