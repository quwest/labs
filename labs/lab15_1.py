# Напишите простой контейнерный класс для небольшой фирмы,
# в которой работает администратор, служащий и рабочий – производные объекты от общего базового класса.

class firma():
    def __init__(self,post=""):
        self.post=post
    def info(self):
        print(self.post)
post=["Администратор","Служащий","Рабочий"]

humans=[]
b = int(input('''Выберете кого создать, где 0-Администратор,1-Служащий,2-Рабочий 3-Выйти из создания'''))
human_x = firma(post[b])
humans.append(human_x.post)





