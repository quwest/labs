class Shape:
    def __init__(self, color, thickness, lenght, width):
        self.color = color
        self.thickness = thickness
        self._size = lenght * width
        self._perimetr = lenght + lenght + width + width
print("Please enter some properties for - Shape, Square, Rectangle")
print("Фигура:")
color = input('Enter color: ')
thickness = int(input('Enter thickness: '))
lenght = int(input('Enter lenght: '))
width = int(input('Enter width: '))

q=Shape(color,thickness,lenght,width)
print(q.__dict__)




class Square(Shape):

    def square_protected_(self, _size):
        self.s = _size

print("Квадрат:")
color = input('Enter color: ')
thickness = int(input('Enter thickness: '))
lenght = int(input('Enter lenght: '))
width = int(input('Enter width: '))
s = Square(color,thickness,lenght,width)
print(s.__dict__)
list = [color,thickness,lenght,width]
print(list)
class Rectangle(Square):

    def rectangle_protected_(self, _size):
        self.s = _size


print("Прямоугольник:")
color = input('Enter color: ')
thickness = int(input('Enter thickness: '))
lenght = int(input('Enter lenght: '))
width = int(input('Enter width: '))
r = Rectangle(color,thickness,lenght,width)
print("shape",q.__dict__)
print("square",s.__dict__)
print("rectangle",r.__dict__)
list = [color,thickness,lenght,width]
print(list)