#Измените программы п.1 и п.2 на циклические.

x = int(input("Введите количество циклов: "))


for i in range(x):

	name = input("Введите Имя фамилию отчество: ")

	name2 = (' '.join(name.split(' ')[:-1]))
	name3 = (' '.join(name2.split(' ')[:-1]))

	surname = (' '.join(name.split(' ')[:-1]))
	surname2 = surname[surname.find(" ") + 1 : ]

	patronymic = name[name.find(" ") + 1 : ]
	patronymic2 = name2[name2.find(" ") + 1 : ]

	print("\nИмя:", name3)
	print("Фамилия:", surname2)
	print("Очество: ", patronymic2, "\n")