class Circle:
    def __init__(self, radius, pi=3.14159):
        self.radius = radius
        self.pi = pi

    def area(self):
        return self.pi * self.radius ** 2

    def circle_len(self):
        return 2 * self.radius * self.pi

circle = Circle(4)

area = circle.area()
print(f'The area of circle is: {area}')

circle_len = circle.circle_len()
print(f'The len of circle is: {circle_len}')