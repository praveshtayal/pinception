# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(string):
    if len(string)<=1:
        return string
    string2 = removeConsecutiveDuplicates(string[1:])
    if string[0]==string[1]:
        return string2
    else:
        return string[0]+string2

# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
