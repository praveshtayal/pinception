def replacePI(s):
    index = s.find('pi')
    if index == -1:
        return s
    return s[:index] + '3.14' + replacePI(s[index+2:])
