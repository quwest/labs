#Напишите программу, считывающую и распечатывающую двоичный файл,
#созданный в п.5. Переменную для чтения объекта определить в стеке (свободной памяти).

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
patronymic =input("Введите очество: ")

l = [name, surname, patronymic]

File = open('File.bin', 'wb')

for item in l:

	s = str(item) + " "
	bt = s.encode()
	File.write(bt)

File.close();


L2 = []

File = open('File.bin', 'rb')

for ln in File:
    x = str(ln)
    L2 = L2 + [x]

print("L2 =", L2)

File.close();