# Напишите небольшую программу с объявлением класса, имеющего одну переменную-член
# и одну статическую переменную-член.
# Пусть конструктор инициализирует переменную-член и инкрементирует статическую переменную член,
# а деструктор – декрементирует ее.

class Human():
    age = 10
    def __init__(self,age):
        self.age = age

    def get_minus_score(self):
        Human.age -= 1

    def get_plus_score(self):
        Human.age += 1
    def __del__(self):
        self.age = self.age - 1
        print(self.age)
h1 = Human
print("1-добавить возраст 2- уменьшить")
a = int(input())
if int(a) == 1:
    print("возраст:")
    h1.get_minus_score(10)
    print(h1.age)
elif a == 2:
    print("возраст:")
    h1.get_plus_score(10)
    print(h1.age)
else:
    print("Ошибка")

