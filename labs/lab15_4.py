# Напишите операторы для вставки и извлечения в поток объектов  класса фирма.
class Firm():
    name = "TOYO"
    def display_info(self):
        print("Hi! name of our firm", self.name)
    def go_to_list_name(self):
        print(list,self.name)

firm = Firm()
firm.display_info()