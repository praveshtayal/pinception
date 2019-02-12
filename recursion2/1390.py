#Problem ID 1390 Return Keypad
def keypad(num):
    options = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    if (num==0):
        lst = [""]
        return lst

    small = num//10
    remainder = num%10
    lst = keypad(small)

    optionslen = len(options[remainder])
    lstlen = len(lst)
    lst *= optionslen
    k=0
    for i in range(0, optionslen):
        for j in range(0, lstlen):
            lst[k] = lst[k] + options[remainder][i]
            k += 1
    return lst

n=int(input())
l=keypad(n)
for str in l:
    print(str)
