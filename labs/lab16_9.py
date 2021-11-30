#Используйте  любой ранее разработанный класс.
#Напишите программу, создающую в цикле несколько
#объектов этого класса в стеке (свободной памяти).
#Запишите эти объекты в двоичный файл.

class Person:

	def set(self, name, surname, proffesion):

		self._protected_member = name
		self._protected_member = surname
		self._protected_member = proffesion


	def __init__(self, name, surname, proffesion, ):

		self.name = name
		self.surname = surname
		self.proffesion = proffesion

	def choice(self):

		if (self.proffesion == 1):

			x = input("Clients: ")
			clients = x
			return("Name:", self.name, "Surname:", self.surname, "Clients:", clients)

		elif(self.proffesion == 2):

			x = input("Workday: ")
			workday = x
			return("Name:", self.name, "Surname:", self.surname, "Workday:", workday)

		elif(self.proffesion == 3):

			x = input("Salary: ")
			salary = x
			return("Name:", self.name, "Surname:", self.surname, "Salary:", salary)



x = int(input("Количество рабортников: "))

for i in range(x):

	print('№',i+1)
	a, b = input("Name, Surname: ").split()
	c = input("Proffesion: ")
	Pr1 = Person(a, b, c)
	l = [str(Pr1.choice())]
	File = open('file2.txt', 'a')

	for index in l:

		File.write(index + '\n')

	File.close()

if (x == 0):

	File = open('file2.txt', 'w')

	File.write(" ")

	File.close()