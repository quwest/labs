#Напишите объявление класса Rectangle (прямоугольник),
# который является производным от Square (квадрат),
# который, в свою очередь – производный от Shape(фигура).
# В классе Shape объявите следующие защищенные члены-данные : цвет линий фигуры и толщина ее линий
# и напишите 2 конструктора - по умолчанию и с параметрами.
# В классах Square и Rectangle объявите закрытые (защищенные) члены-данные для хранения размеров каждой из фигур,
# несколько конструкторов, вызывающих конструкторы базового класса,
# а также методы для вычисления площади и периметра фигур.
# В классе Rectangle обязательно используйте перекрывание методов базового класса Square.
# При необходимости добавьте в классы  методы доступа. Напишите главную программу,
# в которой выполните создание объектов-фигур различных типов и их обработку

class Shape:
    def __init__(self, color, thickness, lenght, width):
        self._color = color
        self._thickness = thickness
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












