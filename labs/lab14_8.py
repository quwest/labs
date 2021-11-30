# Напишите драйвер к п.7,
# в котором создается три объекта и на экран выводятся значения обычной и статической переменных членов класса.
# Уничтожьте эти объекты и проследите как будет меняться значение статической переменной члена.
class Human():
    age = 5
    now_age = ""
    def __init__(self, age, now_age):
        self.now_age = now_age + 1
        self.age = age
    def print(self):
        print(self.now_age,self.age)
    def __del__(self):
        self.now_age = self.now_age-self.now_age
        print("Удаляем человека из б/д")
        print(self.now_age)


h1 = Human(5,13)
print("Возраст:")


print(h1.now_age)

h2 = Human(5,25)
print("Возраст:")

print(h2.now_age)

h3 = Human(5,59)
print("Возраст:")

print(h1.now_age)