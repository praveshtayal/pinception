def digits(num):
    while num:
        yield num%10
        num //= 10
