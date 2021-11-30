#Напишите функции-шаблоны  для :
#удваивания значения объекта любого типов;
# обмена значений двух объектов любых типов;
#определения большего из значений двух объектов любых типов;
#сравнения значений двух объектов любых типов.

class Deistvie():
    def __init__(self,numb1=None,numb2=None):
        self.numb1=numb1
        self.numb2=numb2

    def multiply(self):
        self.numb1= self.numb1 * 2
        print(self.numb1)
    def change(self):
        self.numb1, self.numb2= self.numb2, self.numb1
        print(self.numb1, self.numb2)
    def sravnit(self):
        if self.numb1>self.numb2:
            print(self.numb1)
        else:
            print(self.numb2)
    def ifelse(self):
        if self.numb1>self.numb2:
            print("numb1>numb2")
        elif self.numb1==self.numb2:
            print("numb1==numb2")
        else:
            print("numb2>numb1")

deistvie=Deistvie(1,4)
deistvie.multiply()
deistvie.change()
deistvie.sravnit()
deistvie.ifelse()

