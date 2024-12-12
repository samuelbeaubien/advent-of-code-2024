import numpy as np

def get_num_right_down(arr: np.array, i, j) -> int:
    smaller_arr: np.array = arr[i:i+4, j:j+4]
    row = "".join(smaller_arr[0])
    col = "".join(smaller_arr[:,0].flatten())
    diagonal = "".join(smaller_arr.diagonal())
    inverse_diagonal = "".join(np.rot90(smaller_arr, k=-1).diagonal())
    counter: int = 0
    for s in [row, col, diagonal, inverse_diagonal]:
        if s == "XMAS":
            counter += 1
        elif s == "SAMX":
            counter += 1
    return counter


### main ###

# file = open("src/day-04/example.txt")
file = open("src/day-04/input.txt")
lines = file.readlines()
lines = [list(line.strip()) for line in lines]
arr = np.array(lines)


get_num_right_down(arr, 6, 0)
total = 0
for i, j in np.ndindex(arr.shape):
    total += get_num_right_down(arr, i, j)

print (total)
print("nihao")


