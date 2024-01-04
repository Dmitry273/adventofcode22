class Monkey():
    def __init__(self, items, rule, test, busy = 0):
        self.items = items
        self.rule = rule
        self.test = test
        self.busy = busy

# monkeys = [Monkey([79, 98],
#                   lambda old: (old * 19)%(23*19*13*17),
#                   lambda new: 2 if new%23==0 else 3), 
#            Monkey([54, 65, 75, 74],
#                   lambda old: (old + 6)%(23*19*13*17),
#                   lambda new: 2 if new%19==0 else 0), 
#            Monkey([79, 60, 97],
#                   lambda old: (old * old)%(23*19*13*17),
#                   lambda new: 1 if new%13==0 else 3), 
#            Monkey([74],
#                   lambda old: (old + 3)%(23*19*13*17),
#                   lambda new: 0 if new%17==0 else 1)]
        
worry = 17*19*7*11*13*3*5*2
monkeys = [Monkey([83, 97, 95, 67],
                  lambda old: (old * 19)%worry,
                  lambda new: 2 if new%17==0 else 7), 
           Monkey([71, 70, 79, 88, 56, 70],
                  lambda old: (old + 2)%worry,
                  lambda new: 7 if new%19==0 else 0), 
           Monkey([98, 51, 51, 63, 80, 85, 84, 95],
                  lambda old: (old + 7)%worry,
                  lambda new: 4 if new%7==0 else 3), 
           Monkey([77, 90, 82, 80, 79],
                  lambda old: (old + 1)%worry,
                  lambda new: 6 if new%11==0 else 4),
           Monkey([68],
                  lambda old: (old * 5)%worry,
                  lambda new: 6 if new%13==0 else 5), 
           Monkey([60, 94],
                  lambda old: (old + 5)%worry,
                  lambda new: 1 if new%3==0 else 0), 
           Monkey([81, 51, 85],
                  lambda old: (old * old)%worry,
                  lambda new: 5 if new%5==0 else 1), 
           Monkey([98, 81, 63, 65, 84, 71, 84],
                  lambda old: (old + 3)%worry,
                  lambda new: 2 if new%2==0 else 3)]

def play():
    for monkey in monkeys:
        monkey.busy += len(monkey.items)
        new = list(map(monkey.rule, monkey.items))
        new = list(map(lambda x: x//3, new))
        monkey.items = []
        for a, b in zip(new, list(map(monkey.test, new))):
            monkeys[b].items.append(a)

for _ in range(20):
    play()

answ = list(map(lambda x: x.busy, monkeys))
#print(answ)
answ.sort(reverse= True)
print(answ[0]*answ[1])