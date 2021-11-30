# Напишите объявления для следующих диаграмм классов,
# включив в него члены-данные, конструкторы по умолчанию и с параметрами ,
# методы доступа, методы ввода-вывода для клавиатуры и экрана и т.д. :
# Student(nomer) -> Zaocnik(Mesto raboti)
#                                       Automobil()
# Transport(nomer,god vipuska, marka) ->
#                                       Autobus(Chislo)


class Student():
    def __init__(self, number,name,surname,age,id):
        self.number = number
        self.name = name
        self.surname = surname
        self.age = age
        self._id = id

s1 = Student(14, 'Alex', 'Dobrov', 17, 1236573)
print(s1.__dict__)


class Correspondence_student(Student):
    def __init__(self, number,name,surname,age,id,adress):
        super(Correspondence_student,self).__init__(number, name, surname, age, id)
        self.adress = adress


s2 = Correspondence_student(54, 'Max', 'Belov',18,8574352,'Ushakova')
print(s2.__dict__)



class Transport():
    def __init__(self, number, god, marka):
        self.number = number
        self.god = god
        self.marka = marka



t1 = Transport(2134,2003,'coupe')
print(t1.__dict__)


class Automobil(Transport):
    def auto(self,auto):
        self.auto = auto

t2 = Automobil(7865, 2019, 'BMW')
print(t2.__dict__)


class Autobus(Transport):
    def __init__(self,number,god,marka,chislo):
        super(Autobus,self).__init__(number, god, marka)
        self.chislo=chislo

        self.chislo=chislo
t3 = Autobus(4543, 2010, 'TATA', 5)
print(t3.__dict__)