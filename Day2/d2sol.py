answ = 0
result = [[0,1,-1],[-1,0,1],[1,-1,0]]
for line in open('Day2/d2.txt', 'r'):
    en = ord(line[0]) - 64
    me = ord(line[2]) - 87
    answ += me + 3 + 3*result[en-1][me-1]
print(answ)

answ = 0
result = [[3,1,2],[1,2,3],[2,3,1]]
for line in open('Day2/d2.txt', 'r'):
    en = ord(line[0]) - 64
    me = ord(line[2]) - 87
    answ += result[en-1][me-1] + 3 + 3*(me-2)
print(answ)