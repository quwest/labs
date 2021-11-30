#Напишите объявление статической переменной – члена.
#Напишите определение статической переменной – члена.

class Auto:
    static=0
    def __init__(self, mark, color, horsepower):
        self.mark = mark
        self.color = color
        self.horsepower = horsepower
    def get_info(self):
        print(f"{self.mark} - {self.color} - {self.horsepower}HP")

    @classmethod
    def get_info_class(cls, data):
        mark, color, horsepower = data
        return cls(mark, color, horsepower)
    @staticmethod
    def get_info_static(self):
        print(f"{self.mark} - {self.color} - {self.horsepower}HP")



auto_list=["Mersedes","black","522"]

auto = Auto.get_info_class(auto_list)
#auto.get_info()
auto.get_info_static(auto)