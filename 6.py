embersz = int(input("Adja meg az emberek számát:  "))
ar = int(40000)


csoportos = 0
if embersz >=10 and embersz <= 19:
    csoportos = float(0.05)

elif embersz >=20 and embersz <= 29:
    csoportos = float(0.08)

elif embersz >=30 and embersz <= 40:
    csoportos = float(0.12)

elif embersz >40 :
    csoportos = float(0.14)


intezmenyi = 0
if embersz >=5 and embersz <= 11:
    intezmenyi = int(1)

elif embersz >=12 and embersz <= 19:
    intezmenyi = int(2)

elif embersz >=20 and embersz <= 28:
    intezmenyi = int(3)

elif embersz >=29 and embersz <= 40:
    intezmenyi = int(4)

elif embersz >40:
    intezmenyi = int(5)


diak = float(0.1)


csoportoseredm = (embersz * ar) * (1 - csoportos)

intezmenyieredm = (embersz * ar) - (intezmenyi * ar)

diakeredm = embersz * (ar * (1 - diak))


arak = [csoportoseredm, intezmenyieredm, diakeredm]
arak2 = ["Csoportos", "Intézményi", "Diákkedvezmény"]


print("Csoportos: " + str(csoportoseredm))
print("Intézményi: " + str(intezmenyieredm))
print("Diákkedvezmény: " + str(diakeredm))

legkisebb = arak[0]


for x in arak:
    if x < legkisebb:
        legkisebb = x

print(arak2[arak.index(legkisebb)])