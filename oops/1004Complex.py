# Problem ID 1004 Complex Number Class
class ComplexNumbers:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def plus(self, c):
        self.re += c.re
        self.im += c.im

    def multiply(self, c):
        real = self.re*c.re - self.im*c.im
        self.im = self.re*c.im + self.im*c.re
        self.re = real

    def __str__ (self):
        return str(self.re) + '+ i' + str(self.im)

#main
a, b = [int(i) for i in input().split(' ')]
c1=ComplexNumbers(a, b)
a, b = [int(i) for i in input().split(' ')]
c2=ComplexNumbers(a, b)
choice=int(input())
if choice==1:
    c1.plus(c2)
    print(c1)
else:
    c1.multiply(c2)
    print(c1)
