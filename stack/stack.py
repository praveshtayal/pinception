def checkBalanced(exp):
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

# Problem ID 419 Reverse Stack
def reverseStack(stack, extra):
    # Reverse a given Stack with the help of another empty stack. Two stacks
    # will be given. Out of which first contains some integers and second one is
    # empty. You need to reverse the first one using second stack. Change in the
    # given first stack itself.
    if not stack:
        return
    top=stack.pop()
    reverseStack(stack,extra)
    while stack:
        extra.append(stack.pop())
    stack.append(top)
    while(extra):
        stack.append(extra.pop())

def reverseQueue(queue<int> q):
    # Given a queue of integers, reverse it without help of any explicit stack
    # or queue. You need to change in the given queue itself. 
    if not q:
        return
    front = q.front()
    q.pop()
    reverseQueue(q)
    q.append(front)

# Problem 390 
def checkRedundantBrackets(expr):
    # Given a string mathematical expression, return True if redundant brackets
    # are present in the expression. Brackets are redundant if there is nothing
    # inside the bracket or more than one pair of brackets are present.
    # Assume the given string expression is balanced and contains only one type
    # of bracket i.e. ().
    # Solution: Push brackets as well as operators. Whenever the bracket closes,
    # we must have operators on the stack 
    if(expr==None):
        return False
    s = []
    for char in expr:
        if char is '(':
            s.append(char)
        elif char is ')':
            if(not s or s[-1]!='o'):
                return True
            s.pop(); # pop 'o'
            if(not s or s[-1]!='('):
                return True
            s.pop(); # pop '('
        elif char in '+-/*':
            if(not s or s[-1]!='o'):
                s.append('o')
    #if(not s) return True
    return False

# Problem 86 
def stockSpan(price):
    # The span si of a stock’s price on a certain day i is the minimum number of
    # consecutive days (up to the current day) the price of the stock has been
    # less than its price on that ith day. If for a particular day, if no stock
    # price is greater then just count the number of days till 0th day including
    # current day. 
    # For eg. if given price array is {3, 6, 8, 1, 2}, span for 4th day (which
    # has price 2) is 2 because minimum count of consecutive days (including 4th
    # day itself) from current day which has price less than 4th day is 2 (i.e.
    # day 3 & 4). Similarly, span for 2nd day is 3 because no stock price in
    # left is greater than 2nd day's price. So count is 3 till 0th day.
    # Given an input array with all stock prices, you need to return the array
    # with corresponding spans of each day.
    # Return an array that contain span for each day. For eg for size 8 array:
    # input: 60 70 80 100 90 75 80 120
    # output: 1 2 3 4 1 1 2 8 
    size=len(price)
    s = []
    result = [0] * size
    result[0] = 1
    for i in range(1, size):
        if(price[i]<=price[i-1]):
            result[i] = 1
            s.append(price[i])
            continue
        result[i] = result[i-1]+1
    return result
