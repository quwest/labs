# Напишите дружественную функцию для обработки объекта типа фирма.
class firma():
    def __init__(self,post=""):
        self.post=post
    def info(self):
        print(self.post)
post=["Администратор","Служащий","Рабочий"]

humans=[]
b = int(input('''Выберете кого создать, где 0-Администратор,1-Служащий,2-Рабочий'''))
human_x = firma(post[b])
humans.append(human_x.post)

def FooFriend():
    print("Кто должен получить повышеную зарплату? - ")
    print(humans)
    x=int(input("введите индекс обьекта - "))
    humans[x]=humans[x]+" С повышеной зарплатой в этом месяце"
    print(humans[x])
FooFriend()
human_x.info()