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

# Main
n=int(input())
arr=[int(x) for x in input().split()]
reverseStack(arr, [])
while arr:
    print(arr.pop(), end=' ')
