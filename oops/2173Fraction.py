# Problem ID 2173 Fraction Class
class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()

    def numerator(self):
        return self.numerator

    def denominator(self):
        return self.denominator

    def gcd(a, b):
        minimum = min(a,b)
        ans = 1
        for i in range(2, minimum+1):
            if((a%i)==0 and (b%i)==0):
                ans = i
        return ans

    def reduce(self):
        _gcd = Fraction.gcd(self.numerator, self.denominator)
        self.numerator //= _gcd
        self.denominator //= _gcd

    def plus(self, f):
        self.numerator = self.numerator*f.denominator + f.numerator * self.denominator
        self.denominator = self.denominator * f.denominator
        self.reduce()
        return self

    def multiply(self, f):
        self.numerator *= f.numerator
        self.denominator *= f.denominator
        self.reduce()
        return self

    def __str__ (self):
        return str(self.numerator) + '/' + str(self.denominator)

#main
a, b = [int(i) for i in input().split(' ')]
f1=Fraction(a, b)
a, b = [int(i) for i in input().split(' ')]
f2=Fraction(a, b)
choice=int(input())
if choice==1:
    f1.plus(f2)
    print(f1)
else:
    f1.multiply(f2)
    print(f1)
