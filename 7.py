szoveg = input("Adj meg egy szöveget: ")


if ("iskola" not in szoveg) and ("házi" not in szoveg) and ("tanulás" not in szoveg):
    print(szoveg.upper())
    print(len(szoveg))
else:
    szoveg = szoveg.replace("iskola", "???")
    szoveg = szoveg.replace("házi", "???")
    szoveg = szoveg.replace("tanulás", "???")
    print(szoveg)