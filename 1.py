T = int(input("Adja meg a kezdőtőkét: "))
p = int(input("Adja meg a kamatláb mértékét százalékban: "))
n = int(input("Hány évre teszi be: "))

eredmeny = T * (1 + p / 100) ** n

print(eredmeny)