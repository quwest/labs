# Объявите в главной программе два указателя типа Shape и создайте два объекта типа Square
# и Rectangle в свободной памяти, сохранив их адреса в этих указателях.
# Выполните обработку объектов путем вызова как виртуальных, так и не виртуальных методов классов.
# Уничтожьте объекты и обнулите их указатели.
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
s1= Square(color,thickness,lenght,width)
print(s1.__dict__)
s2 = Square
s2(id)


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
print("square",s1.__dict__)
print("rectangle",r.__dict__)