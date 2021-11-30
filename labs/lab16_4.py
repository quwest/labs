#Используя один из ранее разработанных классов
#(Worker, Student … ), создайте в программе список
#объектов путем ввода данных с клавиатуры и
#рапечатайте его на экране в виде таблицы.
#
#         Список сотрудников (студентов)
#------------------------------------------------------------------------------------
#№        :       Фамилия      :     Возраст     :    Зарплата
#------------------------------------------------------------------------------------
#1.             Иванов               25               500.60
#2.             Петров               30               550.40
#-------------------------------------------------------------------------------------
#                                       Всего :      1051.00

class Person:

    def set(self, name, age, salary):

        self._protected_member = surname
        self._protected_member = age
        self._protected_member = salary


    def __init__(self, surname, age, salary):

        self.surname = surname
        self.age = age
        self.salary = salary

    def print(self):

        print(" "*10, self.surname, " "*(22-len(self.surname)), self.age, " "*27, self.salary)

print("№1")
surname: str = input("Фамилия: ")
age = input("Возраст: ")
salary = input("Зарплата: ")

print("№2")
surname2 = input("Фамилия: ")
age2 = input("Возраст: ")
salary2 = input("Зарплата: ")

Pr1 = Person(surname, age, salary)
Pr2 = Person(surname2, age2, salary)

print("-"*72, "\n", " "*3, ":", " "*3, "Фамилия", " "*5, ":", " "*5, "Возраст", " "*5, ":", " "*5, "Зарплата", "\n", "-"*70)

Pr1.print()
Pr2.print()