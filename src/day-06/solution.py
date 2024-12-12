import numpy as np

def rot90coords(i, j, dim_j):
    new_j = i
    new_i = dim_j - j - 1
    return new_i, new_j

def advance(map: np.array, i: int, j: int):
    new_j = j + 1
    if new_j >= map.shape[1]:
        raise Exception
    val = map[i][new_j]
    if val == '#':
        return False
    else:
        map[i][new_j] = 'x'
        return True

def predict(map: np.array, i: int, j: int):
    while True:
        try:
            if advance(map, i, j):
                j = j+1
            else:
                map = np.rot90(map)
                i, j = rot90coords(i, j, map.shape[1])
        except:
            return map

### main ###
# file = open("src/day-06/example.txt")
file = open("src/day-06/input.txt")
lines = file.readlines()
lines = [list(line.strip()) for line in lines]
map = np.array(lines)
it = np.nditer(map, flags=['multi_index'])
for x in it:
    val = x.item()
    if val == "." or val == "#":
        continue
    else:
        i, j = it.multi_index
        map[i, j] = 'x'
        if val == '^':
            map = np.rot90(map, k=-1)
            i, j = rot90coords(i, j, map.shape[1])
            i, j = rot90coords(i, j, map.shape[1])
            i, j = rot90coords(i, j, map.shape[1])
        elif val == '<':
            map = np.rot90(map, k=2)
            i, j = rot90coords(i, j, map.shape[1])
            i, j = rot90coords(i, j, map.shape[1])
        elif val == '>':
            pass
        else:
            map = np.rot90(map)
            i, j = rot90coords(i, j, map.shape[1])
        break
map = predict(map, i, j)
count = np.count_nonzero(map == 'x')




print("hello")