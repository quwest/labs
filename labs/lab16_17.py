#1Запустите программу п.2 так, чтобы она
#выводила свои результаты не на экран, а в текстовый файл.

name = input("Введите Имя.фамилию.отчество: ")

name2 = (' '.join(name.split(' ')[:-1]))
name3 = (' '.join(name2.split(' ')[:-1]))

surname = (' '.join(name.split(' ')[:-1]))
surname2 = surname[surname.find(" ") + 1 : ]

patronymic = name[name.find(" ") + 1 : ]
patronymic2 = patronymic[patronymic.find(" ") + 1 : ]

l = [name3, surname2, patronymic2]

File = open('file.txt', 'w')

for index in l:

	File.write(index + '\n')

File.close()