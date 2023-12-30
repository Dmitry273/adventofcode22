s = [i for i in open('Day6/d6.txt', 'r')][0]

l = 4
for i in range(len(s)-l):
    if len(set(s[i:i+l])) == l: break
print(i+l)

l = 14
for i in range(len(s)-l):
    if len(set(s[i:i+l])) == l: break
print(i+l)