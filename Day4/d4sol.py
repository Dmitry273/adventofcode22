answ1 = 0
answ2 = 0
for line in open('Day4/d4.txt', 'r'):
    pairs = line[:-1].split(',')
    first = list(map(int, pairs[0].split('-')))
    first = set(range(first[0],first[1]+1))
    second = list(map(int, pairs[1].split('-')))
    second = set(range(second[0],second[1]+1))
    if first.issubset(second) or second.issubset(first): answ1 += 1
    if first & second: answ2 += 1
print(answ1)
print(answ2)