# Напишите программу обработки различных средств транспорта c использование массива указателей типа Transport.
# При обработке  используйте как виртуальные методы, так и средства RTTI.

class Transport():
    def __init__(self,plate,year,mark):
        self.plate = plate
        self.year = year
        self.mark = mark
    def draw(self):
        print(f"Транспорт: {self.plate},{self.year},{self.mark}")
    def printtr(self):
        return "Номер:" + str(self.plate), "Год выпуска: " + str(self.plate), "Марка: " + str(self.mark)
class Car(Transport):
    def __init__(self,color,speed):
        self.color = color
        self.speed = speed


    def printcar(self):
        return "Цвет:"+ str(self.color), "Скорость: " + str(self.speed)


    def draw(self):
        print(f"Вы создали машину: {self.plate},{self.year},{self.mark},{self.color},{self.speed}")
class Sportscar(Car):
    def __init__(self,horsepower):
        self.horsepower = horsepower
    def printcar(self):

        return "ЛС: " + str(self.horsepower)
    def draw(self):
        print(f"Вы создали спорткар: {self.plate},{self.year},{self.mark},{self.horsepower}")
class Wagon(Car):
    def __init__(self,seats):
        self.seats = seats
    def printcar(self):

        return "Количество мест" + str(self.seats)
    def draw(self):
        print(f"Вы создали универсал:  {self.plate},{self.year},{self.mark},{self.seats}")

class Coupe(Car):
    def __init__(self,gear):
        self.gear = gear
    def printcar(self):

        return "Кол-во передач" + str(self.gear)
    def draw(self):
        return (f"Вы создали купе: {self.plate}{self.year}{self.mark}{self.gear}")
cars = []
q = int(input("Введите к-ство транcпортов: "))
i = 1

for i in range(q):

    print("Транспорт №",i+1)


    d = int(input("Что вы хотите создать? 1-Транспорт 2-Машина 3-спорткар 4-универсал 5-купе"))
    a = int(input("Номер: "))
    b = int(input("Год выпуска: "))
    c = str(input("Марка: "))
    T = Transport(a, b, c)
    tr = T.printtr()
    if int(d)==1:
        print("Вы создали транспорт! ")
        #T.draw()
        cars.extend(tr)
        print(cars)
    elif int(d)==2:
        x = str(input("Введите цвет: "))
        y = int(input("Введите максимальную скорость: "))
        #print(T.draw())
        C=Car(x,y)
        cr = C.printcar()
        cars.extend(tr)
        cars.append(cr)
        print(cars)
        #print(C.printcar())
        #print("Вы создали машину! ")

        cars.extend(C.printcar())
    elif int(d)==3:
        g = int(input("Введите число лошадиных сил"))
        #print(T.draw())
        S=Sportscar(g)
        sp = S.printcar()
        cars.extend(tr)
        cars.append(sp)
        print(cars)
        #print(S.printcar())
        #print("Вы создали спорткар! ")
    elif int(d)==4:
        h = int(input("Введите кол-во сидений"))
        #print(T.draw())
        W = Wagon(h)
        wg = W.printcar()
        cars.extend(tr)
        cars.append(wg)
        print(cars)
        #print(W.printcar())
        #print("Вы создали универсал! ")
    elif int(d)==5:
        l = int(input("Введите количество передач"))
        #print(T.draw())
        Co=Coupe(l)
        co = Co.printcar()
        cars.extend(tr)
        cars.append(co)
        print(cars)
        #print(Co.printcar())
        #print("Вы создали купе! ")

    i += 1


