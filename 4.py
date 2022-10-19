dinnyesz = int(input("Dinnyék száma: "))
dinnyeatm = int(input("Dinnyék átlagos átmérője cm-ben: "))
szalaghossz = int(dinnyesz * (dinnyeatm * 2 + 60) / 100)

print(dinnyesz, "dinnyéhez", szalaghossz, "méter szalag kell")