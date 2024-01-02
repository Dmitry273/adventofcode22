import numpy as np

forest = np.array([[int(i) for i in j[:-1]] for j in open('Day8/d8.txt', 'r')])
visibility = np.array([[0 for i in range(len(forest[0]))] for j in range(len(forest))])

def looker():
    for i in range(len(forest)):
        tallest = forest[i][0]
        visibility[i][0] = 1
        for j in range(len(forest[0])):
            if forest[i][j] > tallest:
                tallest = forest[i][j]
                visibility[i][j] = 1
            if tallest == 9: break

for _ in range(4):            
    looker()
    forest = np.rot90(forest)
    visibility = np.rot90(visibility)

print(len(visibility[visibility==1]))
