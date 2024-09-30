class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point{self.x,self.y}"
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    
    def __gt__(self, other):
        if self.x > other.x and self.y > other.y:
            return True
        else:
            return False
    
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
    
    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y)


point1 = Point(1, 2)
point2 = Point(3, 4)
print(point1)
print(point2)
print(point1 == point2)
print(point1 > point2)
print(point1 + point2)
print(point1 - point2)
print(dir(str))
