from datetime import date


birthdate = input("Születési dátum: ")
#ÉÉÉÉ.HH.NN

if len(birthdate) != 10:
    print("Buta vagy")
    exit()

if birthdate[4] != "." and birthdate[7] != ".":
    print("Buta vagy")
    exit()


birthdate = birthdate.split(".") #[xxxx,xx,xx]

today = str(date.today()).split("-")
today = today[0]

x = int(today) - int(birthdate[0])
print(x)


if int(birthdate[1]) == 12 or int(birthdate[1]) <= 2:
    print("Tél")
elif int(birthdate[1]) <= 5 and int(birthdate[1]) >= 3:
    print("Tavesz baktalo")
elif int(birthdate[1]) <= 8 and int(birthdate[1]) >= 6:
    print("Nyár")
else:
    print("Ősz")