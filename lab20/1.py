#Создайте ассоциативный список объектов, распечатайте его и выполните в нем поиск.
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
counter=1
keys=[]
for i in humans:
    keys.append(counter)
    counter+=1







d = {k: [] for k in keys}
counter=1
for i in humans:
    d[counter].append(i)
    counter+=1

while(True):
    name = input("введите имя человека которого хотитe найти")
    found=0

    for i in d.values():


        if i[0]==name:
            print(i,"-найден")
            found=1
            break
    if found==0:
        print('его нету')



