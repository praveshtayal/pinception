class vehicle:
    def __init__(self, color, maxSpeed):
        print('Start: Executing vehicle init')
        super().__init__()
        self.__color = color
        self.__maxSpeed = maxSpeed
        print('End: Executing vehicle init')

    def print(self):
        print(self.__color, self.__maxSpeed)

class private:
    def __init__(self, owner):
        print('Start: Executing private init')
        super().__init__()
        self.__owner = owner
        print('End: Executing private init')

class car(vehicle, private):
    def __init__(self, color, maxSpeed, gears, convertible):
        print('Start: Executing car init')
        super().__init__(color, maxSpeed)
        self.gears = gears
        self.convertible = convertible
        print('End: Executing car init')

    def print(self):
        super().print()
        print(self.gears, self.convertible)

# Main
v = vehicle('Red', 30)
v.print()
c = car('Black', 300, 5, True)
c.print()
