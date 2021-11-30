# Напишите объявление для B747, который является производным от класса JetPlane
class Airplane():
    def __init__(self, metal, color, name, airline):
        self.metal = metal
        self.color = color
        self.name = name
        self.airline = airline
metal = input("Enter metal: ")
color = input("Enter color: ")
name = input("Enter name: ")
airline = input("Enter airline: ")
a1 = Airplane(metal,color,name,airline)
print(a1.__dict__)
class Rocket():
    def __init__(self,company,engine,weight):
        self.company = company
        self.engine = engine
        self.weight = weight
company = input("Enter space company: ")
engine = input("Enter engine: ")
weight = input("Enter weight: ")
r1 = Rocket(company,engine,weight)
print(r1.__dict__)
class JetPlane(Airplane,Rocket):
    def __init__(self,metal,color,name,airline,company,engine,weight,country):
        super(JetPlane,self).__init__(metal=metal,color=color,name=name,airline=airline)
        Rocket.__init__(self, company=company,engine=engine,weight=weight)
        self.country = country
metal = input("Enter metal: ")
color = input("Enter color: ")
name = input("Enter name: ")
airline = input("Enter airline: ")
company = input("Enter company: ")
engine = input("Enter engine: ")
weight = input("Enter weight: ")
country = input("Enter country: ")
j1 = JetPlane(metal,color,name,airline,company,engine,weight,country)
print(j1.__dict__)
class B747(JetPlane):
    def __init__(self,metal,color,name,airline,company,engine,weight,country,passangers):
        super(B747,self).__init__(metal,color,name,airline,company,engine,weight,country)
        self.passangers = passangers
metal = input("Enter metal: ")
color = input("Enter color: ")
name = input("Enter name: ")
airline = input("Enter airline: ")
company = input("Enter company: ")
engine = input("Enter engine: ")
weight = input("Enter weight: ")
country = input("Enter country: ")
passengers = input("Enter passengers: ")
b1 = B747(metal,color,name,airline,company,engine,weight,country,passengers)
print(b1.__dict__)