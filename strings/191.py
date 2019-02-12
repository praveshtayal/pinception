# Problem ID: 191 removeChar
def removeChar(s, character):
    # Note that s.replace(character, '') does the same thing
    ans = ''
    for char in s:
        if char == character:
            continue
        ans += char
    return ans

# Main
s=input()
character=input()
print(removeChar(s, character))
