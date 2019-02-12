class Polynomial:
    # self.degree is the list of degree in ascending order
    # self.coeff is the list of coeff
    def __init__(self):
        self.degree = []
        self.coeff = []

    def setCoefficient(self, degree, coeff):
        if degree in self.degree:
            index = self.degree.index(degree)
            if(coeff==0):
                self.degree.pop(index)
                self.coeff.pop(index)
            else:
                self.coeff[index] = coeff
        else:
            if(coeff==0):
                return self
            index = self.getCoefficientIndex(degree)
            self.degree.insert(index, degree)
            self.coeff.insert(index, coeff)

    def add(self, b):
        for i in range(0, len(b.degree)):
            degree = b.degree[i]
            coeff = self.getCoefficient(degree)
            coeff += b.coeff[i]
            self.setCoefficient(degree, coeff)
        return self

    def subtract(self, b):
        for i in range(0, len(b.degree)):
            degree = b.degree[i]
            coeff = self.getCoefficient(degree)
            coeff -= b.coeff[i]
            self.setCoefficient(degree, coeff)
        return self

    def multiply(self, b):
        import copy
        old = copy.deepcopy(self)
        self.degree = []
        self.coeff = []
        for i in range(0, len(b.degree)):
            degreeB = b.degree[i]
            coeffB = b.coeff[i]
            for j in range(0, len(old.degree)):
                degreeA = old.degree[j]
                coeffA = old.coeff[j]
                temp = Polynomial()
                temp.setCoefficient(degreeA+degreeB, coeffA*coeffB)
                self.add(temp)
        return self

    def getCoefficient(self, degree):
        index=self.getCoefficientIndex(degree)
        if(index<len(self.degree) and self.degree[index] == degree):
            return self.coeff[index]
        return 0

    def __str__(self):
        s = ''
        for deg, coef in zip(self.degree,self.coeff):
            s += str(coef) + 'x' + str(deg) + ' '
        return s

    def getCoefficientIndex(self, degree):
        for i in range(0, len(self.degree)):
            if(self.degree[i] >= degree):
                return i
        return len(self.degree)

# Main
count1 = int(input())
degree1=list(int(i) for i in input().strip().split(' '))
coeff1=list(int(i) for i in input().strip().split(' '))
first = Polynomial()
for deg, coef in zip(degree1,coeff1):
    first.setCoefficient(deg,coef)

count2 = int(input())
degree2=list(int(i) for i in input().strip().split(' '))
coeff2=list(int(i) for i in input().strip().split(' '))
second = Polynomial()
for deg, coef in zip(degree2,coeff2):
    second.setCoefficient(deg,coef)

choice = int(input())
if choice==1:
    first.add(second)
    print(first)
elif choice==2:
    first.subtract(second)
    print(first)
elif choice==3:
    first.multiply(second)
    print(first)
