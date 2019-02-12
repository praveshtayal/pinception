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
    s = [0]
    result = [1] * size
    for i in range(1, size):
        if(price[i]<=price[i-1]):
            s.append(i)
        else:
            result[i] = result[i-1]+1
            while s and price[i] > price[s[-1]]:
                index = s.pop()
                result[i] = i - index + 1
            if not s:
                s = [0]
    return result

# Main
n=int(input())
arr=[int(x) for x in input().split()]
result=stockSpan(arr)
for num in result:
    print(num, end=' ')
