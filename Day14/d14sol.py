lines = [i[:-1].split(' -> ') for i in open('Day14/d14.txt', 'r')]
rocks = set()
bottom = float('-inf')

for line in lines:
    for i in range(len(line)-1):
        a = [int(n) for n in line[i].split(',')]
        b = [int(n) for n in line[i+1].split(',')]
        bottom = max(a[1],b[1],bottom)
        if a[0] == b[0]:
            l = min(a[1], b[1])
            r = max(a[1], b[1])
            for num in range(l, r+1):
                rocks.add((a[0], num))
        else:
            l = min(a[0], b[0])
            r = max(a[0], b[0])
            for num in range(l, r+1):
                rocks.add((num, a[1]))

t1 = len(rocks)

end = 0
while 1:
    sand = (500,0)
    if sand in rocks: break
    while 1:
        if sand[1] >= bottom:
            end = 1
            break
        if (sand[0],sand[1]+1) not in rocks:
            sand = (sand[0],sand[1]+1)
            continue
        if (sand[0]-1,sand[1]+1) not in rocks:
            sand = (sand[0]-1,sand[1]+1)
            continue
        if (sand[0]+1,sand[1]+1) not in rocks:
            sand = (sand[0]+1,sand[1]+1)
            continue
        rocks.add(sand)
        break
    if end: break
    
t2 = len(rocks)
print(t2-t1)

while 1:
    sand = (500,0)
    if sand in rocks: break
    while 1:
        if sand[1] == bottom+1:
            rocks.add(sand)
            break
        if (sand[0],sand[1]+1) not in rocks:
            sand = (sand[0],sand[1]+1)
            continue
        if (sand[0]-1,sand[1]+1) not in rocks:
            sand = (sand[0]-1,sand[1]+1)
            continue
        if (sand[0]+1,sand[1]+1) not in rocks:
            sand = (sand[0]+1,sand[1]+1)
            continue
        rocks.add(sand)
        break

t3 = len(rocks)
print(t3-t1)