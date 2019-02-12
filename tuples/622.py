def uniqueChars(string):
    m={}
    ans = ''
    for char in string:
        if char not in m:
            m[char] = 1
            ans += char
    return ans

# Main
string = input()
print(uniqueChars(string))
