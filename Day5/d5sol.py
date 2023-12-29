flip = 0
commands = []
content = []

for line in open('Day5/d5.txt', 'r'):
    if not line[:-1]:
        flip = 1
        continue
    if flip: commands.append(line[:-1])
    else: content.append([i for i in line[:-1]])

def mover(fr, to):
    piece = content[fr-1].pop(-1)
    content[to-1].append(piece)

for action in commands:
    num = int(action.split()[1])
    fr = int(action.split()[3])
    to = int(action.split()[5])
    for _ in range(num):
        mover(fr, to)

answ = ''
for line in content:
    answ += line[-1]
print(answ)