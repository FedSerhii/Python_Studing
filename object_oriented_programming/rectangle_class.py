class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def area(self):
        return self.width * self.length

    def perimetr(self):
        return 2 * (self.width + self.length)


rectangle = Rectangle(10, 4)

perimetr = rectangle.perimetr()
print('Perimetr of rectangle is: ', perimetr)

area = rectangle.area()
print('The area of rectangle is: ', area)