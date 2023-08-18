# Craete the Main Class for Points (x,y)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def fal_in_rec(self, rectangle):
        if rectangle.lowleft.x < self.x\
        < rectangle.upright.x \
        and rectangle.lowleft.y < self.y \
        < rectangle.upright.y:
            return True
        else:
            return False

# Secondary class for rectangle shapes & Coordinates

class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def area(self):
        return (self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y)

# Create a random value for the X and Y axis

from random import randint
rectangle = Rectangle(Point(randint(0,9), randint(0,9)), Point(randint(10,19), randint(10, 19)))
print('Rectangle Coordinates: ', rectangle.lowleft.x, ",", rectangle.lowleft.y, "and",
      'and', rectangle.upright.x, ",", rectangle.upright.y)

usr_point = Point(float(input('Guess X: ')),
                  float(input('Guess Y: ')))

usr_area = float(input('Guess the area'))

print('Your point was inside the rectangle: ', 
      usr_point.fal_in_rec(rectangle))

print('Your guessed area exceed by', rectangle.area() - usr_area)
