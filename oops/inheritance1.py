class circle:
    pi = 3.14
    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return circle.pi * (self.radius**2)

class Cylinder(circle):
    def __init__(self, radius=1, ht=1):
        super().__init__(radius)
        self.height = ht

    def volume(self):
        return self.area() * self.height

# Main
c = circle()
C = Cylinder()
print(C.area())
print(C.volume())
