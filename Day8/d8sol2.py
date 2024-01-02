import numpy as np

forest = np.array([[int(i) for i in j[:-1]] for j in open('Day8/d8.txt', 'r')])
visibility = np.array([[0 for i in range(len(forest[0]))] for j in range(len(forest))])

def looker(arr):
    top = arr[0]
    count = 0
    for i in range(1,len(arr)):
        count += 1
        if arr[i] >= top: break
    return count


for i in range(len(forest)):
    for j in range(len(forest[0])):
        R, L, U, D = forest[i:,j], forest[:i+1,j][::-1], forest[i,:j+1][::-1], forest[i,j:]
        visibility[i][j] = looker(R)*looker(L)*looker(U)*looker(D)

print(max(visibility.flatten()))
