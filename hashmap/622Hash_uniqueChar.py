# Problem ID 622: unique char in string
def uniqueChar(s):
    ans = ''
    m = {}
    for char in s:
        if char not in m:
            ans = ans + char
            m[char] = True
    return ans

# Main
s=input()
print(uniqueChar(s))
