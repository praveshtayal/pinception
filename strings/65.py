# Problem ID: 65 compress string
def compress(s):
    ans = s[0]
    i, length = 1, len(s)
    while i<length:
        if ans[-1]==s[i]:
            count = 2
            i += 1
            while i<length and ans[-1]==s[i]:
                count += 1
                i += 1
            ans += str(count)
        else:
            ans += s[i]
            i += 1
    return ans

# Main
s=input()
print(compress(s))
