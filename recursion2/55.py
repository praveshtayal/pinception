# Problem ID 55 Check AB
def checkA(str):
    if(len(str)==0):
        return True
    if(str[0]=='a'):
        return checkA(str[1:])
    if(str[0]=='b'):
        if(len(str)==1):
            return False
        if(str[1]=='b'):
            return checkBB(str[2:])
    return False

def checkBB(str):
    if(len(str)==0):
        return True
    if(str[0]=='a'):
        return checkA(str[1:])
    return False

def checkAB(str):
    if(len(str)==0):
        return False
    if(str[0]!='a'):
        return False
    return checkA(str[1:])

str=input()
if(checkAB(str)):
    print("true")
else:
    print("false")
