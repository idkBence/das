import math


szelesseg = float(input("Adja meg a terület szélességét méterben: "))
hossz = float(input("Adja meg a terület hosszát méterben: "))
terulet = float(szelesseg * hossz)

lapmennyiseg = terulet / (40 * 40 / 1000)
print(float(lapmennyiseg))

veger = lapmennyiseg / 10
print(int(math.ceil(veger)))