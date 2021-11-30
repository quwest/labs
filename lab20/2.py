#Создайте множество объектов, распечатайте его и выполните в нем поиск.
class Human():
    def __init__(self,name):
        self.name=name
    def print_name(self):
        print(self.name)
humans=[]
while(True):
    name=input('введите имя человека, чтобы прекратить нажмите любую цифру')
    try:
        int(name)
    except:
        pass
    else:
        break
    human=Human(name)
    humans.append(human.name)


#set
list1=set(humans)

while(True):
    name = input("введите имя человека которого вы хотите найти")
    found=0
    for value in list1:

        if value == name:
            print(value, "вот он")
            found=1
            break
    if found==0:
        print(name + " не найден")