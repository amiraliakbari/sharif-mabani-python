import math

class Circle:
    def __init__(self, r, x=0, y=0):
        self.r = r
        self.x = x
        self.y = y

    def get_area(self):
        return self.r**2 * 3.14

    def get_diam(self):
        return self.r * 2 * 3.14

c1 = Circle(r=1, x=0, y=0)
c2 = Circle(3)

print c1.get_area()
print c2.get_area()

#r = 1
#c1.r = 2
#c2.r = 3