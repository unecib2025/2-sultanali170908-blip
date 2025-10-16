#1
a = input("Введите пароль: ")
b = len(a)

if b < 8:
    print("Слишком короткий пароль")

if b >= 8:
    print("Пароль принят")
    
#2
status = input("Введите статус сервера (online/offline): ")

if status == "online":
    print("Связь установлена")
else:
    print("Связь потеряна")

#3
a=int(input()) #ueoven uqrozi
if 1<a<=30:
	print("nizkiy")
elif 31<=a<=70:
	print("sredniy")
else:
	print("kriticeskiy")

#4
checksum_original= input()
checksum_current=input()
status="fayl ne izmenen" if checksum_original==checksum_current else "fayl povrejden"
print(status)

#5
event_code = input("Введите код события: ")

match event_code:
    case "ERR":
        print("Ошибка системы")
    case "WRN":
        print("Предупреждение")
    case "INF":
        print("Информационное сообщение")
    case _:
        print("Неизвестный код события")
