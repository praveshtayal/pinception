# Problem ID 418 Stack: Balanced Paranthesis
def checkBalanced(expr):
    # Given a string expression, check if brackets present in the expression are
    # balanced or not. Brackets are balanced if the bracket which opens last,
    # closes first. You need to return True if it is balanced, false otherwise.
    # For eg: { a + [ b+ (c + d)] + (e + f) } => True
    # and { a + [ b - c } ] => false 
    s = []
    for char in expr:
        if char in '({[':
            s.append(char)
        elif char is ')':
            if(not s or s[-1]!='('):
                return False
            s.pop()
        elif char is '}':
            if(not s or s[-1]!='{'):
                return False
            s.pop()
        elif char is ']':
            if(not s or s[-1]!='['):
                return False
            s.pop()
    if not s:
        return True
    return False

# Main
exp=input()
if checkBalanced(exp):
    print('true')
else:
    print('false')
