cals = []
local = 0
for line in open('Day1/d1.txt', 'r'):
    if line[:-1]: local += int(line[:-1])
    else:
        cals.append(local)
        local = 0
cals.sort(reverse= True)
print(cals[0])
print(sum(cals[0:3]))