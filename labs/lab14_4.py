#Измените п.3 так, как если бы функция была членом класса  Car.
class Car:

    def print_two_numbers(x,y):
        print(int(x))
        print(int(y))

x = float(input("x: "))
y = float(input("y: "))
Car.print_two_numbers(x,y)
print(Car.__dict__)