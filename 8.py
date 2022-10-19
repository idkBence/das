# 10cm
import math

commands = input("Utasítás: ")
commArray = []
for x in commands:
    commArray.append(x)

start = [0,0]
pos = [0,0]

for x in commArray:
    if x == "E":
        pos[1] += 10
    elif x == "D":
        pos[1] -= 10
    elif x == "K":
        pos[0] += 10
    else:
        pos[0] -= 10

distance = math.sqrt( ((start[0]-pos[0])**2)+((start[1]-pos[1])**2) )

print(distance)

print(pos)