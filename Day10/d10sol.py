signal = [int(i[:-1][4:]) if i[:-1][4:] else 0 for i in open('Day10/d10.txt', 'r')]
decoded = []
for s in signal:
    decoded.append(0)
    if s!=0: decoded.append(s)

i = 0
x = 1
answ = 0
while i < 240:
    x += decoded[i]
    i += 1
    if (i-19)%40 == 0: answ += x*(i+1)
print(answ)

i = 0
x = 1
CRT = [[' ' for i in range(40)] for j in range(6)]
while i < 240:
    x += decoded[i]
    i += 1
    if abs(i%40-x) <= 1: CRT[i//40][i%40] = '\u2588'

for line in CRT:
    print(''.join(line))