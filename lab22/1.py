#Используя ранее разработанные иерархии классов (Animal, Transport, Worker, Student…), создайте в программе общий контейнер (массив, вектор, список…)
# объектов различных типов
class Human:
    def __init__(self, age=None, gender=None, name=None):
        self._age = age
        self._gender = gender
        self._name = name
        self._age = input("Введите возраст человека - ")
        self._gender = input("Введите пол человека - ")
        self._name = input("Введите имя человека - ")

    def GetInfo(self):
        print(self._name +" , "+ self._gender + "возраст: " + self._age)


class Teacher(Human):
    def __init__(self, subj=None, age=None, gender=None, name=None):
        super().__init__(age, gender, name)
        self._subj = input("Введите предмет учителя - ")




    def GetInfo1(self):
        print("учитель " + self._name + " " + self._gender + "возраст: " + self._age+'предмет: '+ self._subj)
q = Human()
q.GetInfo()
t = Teacher()
t.GetInfo1()



list=[q,t]
print(list)