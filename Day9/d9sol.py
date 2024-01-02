visited = set()
head, tail = (0,0), (0,0)
moves = {'R': (1,0), 'L': (-1,0), 'U': (0,1), 'D': (0,-1)}

def summ(a, b):
    if len(a) != len(b): return 'error'
    return tuple(a[i]+b[i] for i in range(len(a)))

def farr(a, b):
    return abs(a[0]-b[0]) > 1 or abs(a[1]-b[1]) > 1

for move in open('Day9/d9.txt', 'r'):
    for _ in range(int(move[2:])):
        prev = tuple([i for i in head])
        head = summ(head, moves[move[0]])
        if farr(head, tail): tail = prev
        visited.add(tail)

print(len(visited))