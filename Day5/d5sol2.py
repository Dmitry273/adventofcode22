flip = 0
commands = []
content = []

for line in open('Day5/d5.txt', 'r'):
    if not line[:-1]:
        flip = 1
        continue
    if flip: commands.append(line[:-1])
    else: content.append([i for i in line[:-1]])

def mover(fr, to, num):
    pieces = content[fr-1][-num:]
    for _ in range(num):
        content[fr-1].pop(-1)
    content[to-1] += pieces

for action in commands:
    num = int(action.split()[1])
    fr = int(action.split()[3])
    to = int(action.split()[5])
    mover(fr, to, num)

answ = ''
for line in content:
    answ += line[-1]
print(answ)