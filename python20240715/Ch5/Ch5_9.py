class Point:
    def __init__(self, x = 0,y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)
    def __lt__(self,other):
        self_msg =(self.x ** 2) + (self.y ** 2 )
        other_msg = (other.x ** 2) + (other.y ** 2)
        return self_msg < other_msg

p1 = Point(1,1)
p2 = Point(-2,-3)
print(p1 < p2)
