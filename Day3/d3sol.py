rucksacks = [i[:-1] for i in open('Day3/d3.txt', 'r')]

answ = 0
for letters in rucksacks:
    l = len(letters)//2
    first = set(letters[:l])
    second = set(letters[l:])
    wrong = (first & second).pop()
    if wrong.lower() == wrong: answ += 1 + ord(wrong) - ord('a')
    else: answ += 27 + ord(wrong) - ord('A')
print(answ)

answ = 0
for i in range(len(rucksacks)//3):
    first = set(rucksacks[3*i])
    second = set(rucksacks[3*i+1])
    third = set(rucksacks[3*i+2])
    badge = (first & second & third).pop()
    if badge.lower() == badge: answ += 1 + ord(badge) - ord('a')
    else: answ += 27 + ord(badge) - ord('A')
print(answ)