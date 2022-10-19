szoveg = input("Adjon meg egy szöveget: ")

szoveg = szoveg.split(" ")
print(len(szoveg))

for x in range(len(szoveg)):
    szoveg[x] = szoveg[x].replace(",", "")

print(szoveg)