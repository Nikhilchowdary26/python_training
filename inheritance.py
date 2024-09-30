class GrandFather:

    def __init__(self, yards=1):
        self.yards = yards

    def plot(self):
        print(f"(GrandFather has a {self.yards} plot)")


class GrandMother:
    def __init__(self, gold=1):
        self.gold = gold

    def gold(self):
        print(f"(GrandMother has {self.gold} gms of gold")


class Father(GrandFather, GrandMother):

    def __init__(self, cars=1, yards=2, gold=1):
        GrandFather.__init__(self, yards)
        GrandMother.__init__(self, gold)
        self.cars = cars

    def cars(self):
        print(f"(Father has {self.cars} cars)")


class Son(Father):

    def __init__(self, yards=3, cars=2, houses=0,gold=1):
        super().__init__(yards, cars)
        self.houses = houses

    def __str__(self):
        if self.houses == 0:
            return f"Son has {self.yards} yards, {self.cars} cars and {self.gold} gms of gold"
        else:
            return f"Son has {self.yards} yards, {self.cars} cars, {self.gold} gms of gold and {self.houses} house(s)"

    def houses(self):
        print(f"(Son has {self.houses} houses)")


son = Son(houses=1)
son1 = Son()
son1.gold=100
print(son1)
