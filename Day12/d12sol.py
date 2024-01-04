from collections import defaultdict
from queue import PriorityQueue

terrain = []
for i, line in enumerate(open('Day12/d12.txt', 'r')):
    chars = line[:-1]
    if 'S' in chars: start = (i, chars.find('S'))
    if 'E' in chars: end = (i, chars.find('E'))
    chars = chars.replace('S', 'a')
    chars = chars.replace('E', 'z')
    terrain.append([ord(s) for s in chars])

def inside(coor):
    return all([0 <= coor[0], coor[0] < len(terrain), 0 <= coor[1], coor[1] < len(terrain[0])])

def manageable(coor, elevation):
    return terrain[coor[0]][coor[1]] <= elevation + 1

def neighbors(coor):
    elevation = terrain[coor[0]][coor[1]]
    answ = [(coor[0]+1, coor[1]), (coor[0]-1, coor[1]), (coor[0], coor[1]+1), (coor[0], coor[1]-1)]
    answ = list(filter(inside, answ))
    answ = list(filter(lambda x: manageable(x, elevation), answ))
    return answ

def pathfinder(start):
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    potential = PriorityQueue()
    potential.put((distances[start], start))

    while not potential.empty():
        L, curr = potential.get()
        if L > distances[curr]: continue

        L += 1
        new = neighbors(curr)
        for each in new:
            if L >= distances[each]: continue
            else: distances[each] = L
            if each == end: continue
            else: potential.put((L, each))

    return distances[end]

print(pathfinder(start))

answ = []
for i in range(len(terrain)):
    for j in range(len(terrain[0])):
        if terrain[i][j] == ord('a'): answ.append(pathfinder((i, j)))

print(min(answ))