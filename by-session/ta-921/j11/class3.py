class Circle:
    def __init__(self, r, x=0, y=0):
        self.r = r
        self.x = x
        self.y = y

    def get_area(self):
        return self.r**2 * 3.14

    def get_diam(self):
        return self.r * 2 * 3.14

class Rectangle:
    def __init__(self, w, h, x=0, y=0):
        self.w = w
        self.h = h
        self.x = x
        self.y = y

    def get_area(self):
        return self.w * self.h

class Home(Rectangle):
    def __init__(self, w, h, pelak):
        super(Home, self).__init__(w, h)
        self.pelak = pelak

    def get_price(self):
        return self.get_area * 100


a = input()
b = input()
h1 = Home(a, b, pelak='9')
#print h1.get_area()
print h1.get_price()






