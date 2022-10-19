import random


buza = int(input("Adja meg az elvetett búza mennyiségét tonnában: "))
szorzo = random.randint(5, 15)
eredmeny = buza * szorzo

print(eredmeny)
print(szorzo)

if szorzo >= 5 and szorzo <= 8:
    print("Átlag alatti")
elif szorzo >= 9 and szorzo <= 12:
    print("Átlagos év")
elif szorzo >= 13 and szorzo <= 15:
    print("Átlag feletti év")