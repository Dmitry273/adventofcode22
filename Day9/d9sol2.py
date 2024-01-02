moves = {'R': (1,0), 'L': (-1,0), 'U': (0,1), 'D': (0,-1)}

def summ(a, b):
    return (a[0]+b[0], a[1]+b[1])

def subb(a, b):
    return (a[0]-b[0], a[1]-b[1])

def farr(a, b):
    return abs(a[0]-b[0]) > 1 or abs(a[1]-b[1]) > 1

def ropesim(num):
    visited = set()
    rope = [(0,0) for i in range(num)]
    for move in open('Day9/d9.txt', 'r'):
        for _ in range(int(move[2:])):
            teleport = moves[move[0]]
            prev = rope[0]
            rope[0] = summ(rope[0], teleport)
            for i in range(1,len(rope)):
                prev1 = rope[i]
                if farr(rope[i-1],rope[i]):
                    if teleport in moves.values():
                        rope[i] = prev
                    else:
                        if rope[i][0]-rope[i-1][0] == 0:
                            rope[i] = (rope[i][0],(rope[i][1]+rope[i-1][1])//2)
                        elif rope[i][1]-rope[i-1][1] == 0:
                            rope[i] = ((rope[i][0]+rope[i-1][0])//2,rope[i][1])
                        else:
                            rope[i] = summ(rope[i], teleport)
                else: break
                prev = prev1
                teleport = subb(rope[i], prev1)
            visited.add(rope[-1])
    return len(visited)

print(ropesim(2))
print(ropesim(10))