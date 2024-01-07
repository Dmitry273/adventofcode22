import re

beacons = set()
sensors = set()
borders = [float('inf'),float('-inf'),float('inf'),float('-inf')]

for line in open('Day15/d15.txt', 'r'):
    coors = [int(i) for i in re.findall('([0-9-]+)', line)]
    borders[0] = min(borders[0], coors[0], coors[2])
    borders[1] = max(borders[1], coors[0], coors[2])
    borders[2] = min(borders[2], coors[1], coors[3])
    borders[3] = max(borders[3], coors[1], coors[3])
    beacon = (coors[2],coors[3])
    sensor = (coors[0],coors[1],abs(coors[0]-coors[2])+abs(coors[1]-coors[3]))
    sensors.add(sensor)
    beacons.add(beacon)

def ranger(y, sensor):
    delta = sensor[2]-abs(sensor[1]-y)
    if delta >= 0: return [sensor[0] - delta, sensor[0] + delta]
    pass

def merge(arr):
    if len(arr) == 1: return arr

    answ = [[j for j in i] for i in sorted(arr, key= lambda x: (x[0],-x[1]))] #fucking retarded piece of shit, why
    i = 1
    while 1:
        if len(answ) <= i: break

        if answ[i][1] <= answ[i-1][1]:
            answ.pop(i)
        elif answ[i][0] <= answ[i-1][1]:
            answ[i-1][1] = answ[i][1]
            answ.pop(i)
        else:
            i += 1

    return answ


Y = 2000000

pile = []
for sensor in sensors:
    ran = ranger(Y, sensor)
    if ran:
        pile.append(ran)
pile = merge(pile)
print(pile[0][1]-pile[0][0])

for Y in range(4000001):
    pile = []
    for sensor in sensors:
        ran = ranger(Y, sensor)
        if ran:
            pile.append(ran)

    alt1 = merge(pile)
    alt = merge(pile+[[0,4000000]])
    if alt1 != alt:
        print(Y+((alt1[0][1]+1)*4000000))
        break
