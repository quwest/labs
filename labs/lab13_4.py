# Модифицируйте программу п.3 так, чтобы Car был ADT,
# и выведите из Car классы SportsCar, Wagon, Coupe.
# Реализуйте в классах простейшие функции.
class Transport():
    def __init__(self,plate,year,mark):
        self.plate = plate
        self.year = year
        self.mark = mark
    def draw(self):
        print(f"Транспорт: {self.plate},{self.year},{self.mark}")
class Car(Transport):
    def __init__(self,color,speed):
        self.color = color
        self.speed = speed


    def printcar(self):
        print("Цвет и скорость: ")
        return (str(self.color),str(self.speed) + " км/час")


    def draw(self):
        print(f"Вы создали машину: {self.plate},{self.year},{self.mark},{self.color},{self.speed}")


class Sportscar(Car):
    def __init__(self,horsepower):
        self.horsepower = horsepower
    def printcar(self):
        print("Лошадиные силы: ")
        return (str(self.horsepower) + " лс")
    def draw(self):
        print(f"Вы создали спорткар: {self.plate},{self.year},{self.mark},{self.horsepower}")


class Wagon(Car):
    def __init__(self,seats):
        self.seats = seats
    def printcar(self):
        print("Количество сидений: ")
        return (str(self.seats)+ " мест")
    def draw(self):
        print(f"Вы создали универсал:  {self.plate},{self.year},{self.mark},{self.seats}")

class Coupe(Car):
    def __init__(self,gear):
        self.gear = gear
    def printcar(self):
        print("Количество передач: ")
        return (str(self.gear)+ " ступенчатая")
    def draw(self):
        print(f"Вы создали купе: {self.plate}{self.year}{self.mark}{self.gear}")

d = int(input("Что вы хотите создать? 1-Транспорт 2-Машина 3-спорткар 4-универсал 5-купе"))
a = int(input("Номер: "))
b = int(input("Год выпуска: "))
c = str(input("Марка: "))
T = Transport(a, b, c)
if int(d)==1:
    print("Вы создали транспорт! ")
    T.draw()
elif int(d)==2:
    x = str(input("Введите цвет: "))
    y = int(input("Введите максимальную скорость: "))
    print(T.draw())
    C=Car(x,y)
    print(C.printcar())
    print("Вы создали машину! ")
elif int(d)==3:
    g = int(input("Введите число лошадиных сил"))
    print(T.draw())
    S=Sportscar(g)
    print(S.printcar())
    print("Вы создали спорткар! ")
elif int(d)==4:
    h = int(input("Введите кол-во сидений"))
    print(T.draw())
    W = Wagon(h)
    print(W.printcar())
    print("Вы создали универсал! ")
elif int(d)==5:
    l = int(input("Введите количество передач"))
    print(T.draw())
    Co=Coupe(l)
    print(Co.printcar())
    print("Вы создали купе! ")
