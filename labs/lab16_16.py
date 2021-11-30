#Напишите программу, которая принимает параметр –
#имя текстового файла и открывает его для чтения.
#Если файла нет – печатает сообщение и завершает работу.
#Прочитайте все символы из этого файла, но выводите на экран только русские буквы и знаки препинания.
import codecs

def checkRus(string):
    alphabet = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о", "п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
    for one_char in string:
        if one_char in alphabet:
            return True
    return False

a = input("Введите имя файла: ")

try:
	File = open(a, 'r')

except:
	print("Tакого файла не существует.")
	exit()

for line in File:
    for letter in line:
	    if checkRus(letter) == True:
		    print(letter,end='')
    print("\n")

