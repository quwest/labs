# Напишите программу, в которой классы Car и Bus будут производными от класса Transport,
# а MicroBus – производным от  Car и Bus.
# Сделайте Transport абстрактным типом данных с двумя чисто виртуальными функциями.
# Классы Car и Bus не должны быть ADT. Проверьте программу, путем создания объектов разных типов

class Transport():
    def draw(self):
        print("We made transport")
    def draw(self):
        print("Whish you made a car?")
t1 = Transport()
#t1.draw()
class Car(Transport):
    def __init__(self,color,nomer,year,type1):

        self.color = color
        self.nomer = nomer
        self.year = year
        self.type1 = type1
    def draw(self):
        print(f"Создание машины: {self.color},{self.nomer},{self.year},{self.type1}")
c1 = Car("Resonant pink",2345,2018,'coupe')
#print(c1.__dict__)
class Bus(Transport):
    def __init__(self,country,passangers):

        self.country = country
        self.passangers = passangers
    def draw(self):
        print(f"Создание автобуса: {self.country},{self.passangers}")
b1 = Bus("Ukraine",25)
#print(b1.__dict__)
class MicroBus(Car,Bus):
    def __init__(self,color,nomer,year,type1,country,passangers,doors):
        super(MicroBus, self).__init__(color=color,nomer=nomer,year=year,type1=type1)
        b1.__init__(country=country,passangers=passangers)
        self.doors=doors
    def draw(self):
        print(f"Создание микро-автобуса: {self.color},{self.nomer},{self.year},{self.type1},{self.doors}")
m1=MicroBus("red",2345,2005,"microbus","UA",10,6)
#print(m1.__dict__)

cars = []
cars.append(t1)
cars.append(c1)
cars.append(b1)
cars.append(m1)
for f in cars:
    f.draw()
