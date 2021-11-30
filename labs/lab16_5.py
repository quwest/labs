#5.	Напишите программу, предлагающую пользователю ввести его фамилию,
#имя и отчество , а затем выводящую эти сведения в текстовый файл.

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
middlename =input("Введите очество: ")

l = [name, surname, middlename]

File = open('file.txt', 'w')

for i in l:

	File.write(i + '\n')

File.close()