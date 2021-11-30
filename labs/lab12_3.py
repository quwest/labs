# Измените классы Shape->Square->Rectangle из предыдущего задания на виртуальные.
# Для этого добавьте в класс Shape пустые методы для вычисления площади и периметра
# и перекройте их виртуальными методами в производных классах. Не забудьте также и про виртуальные деструкторы.



class Shape():
    def __init__(self,lenght, width):
        self.lenght = lenght
        self.width = width
    def parametr(self,size,perimetr):
        pass

q = Shape(12,34)
print(q.__dict__)
class Square(Shape):
    def parametr(self,size,perimetr):
        self.size = self.lenght * self.width
        self.perimetr = (self.lenght + self.width) * 2

s = Square(12,45)
s.parametr(0,0)
print(s.__dict__)

class Rectangle(Square):
    def parametr(self,size,perimetr):
        self.size = self.lenght * self.width
        self.perimetr = (self.lenght + self.width) * 2
r = Rectangle(15,34)
r.parametr(0,0)
print(r.__dict__)