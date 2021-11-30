#Напишите набор простейших классов для создания личных исключений,
# возникающих при работе с объектом типа
# Student (Worker, Pencil, Animal, Cat …, см. л.р. №17, №18).
class Cifra(Exception):
    def __init__(self, text):
        self.text = text

a = input("input number")
try:
    int(a)
except:
    raise Cifra("You gave not int!")

else:
    print(a)