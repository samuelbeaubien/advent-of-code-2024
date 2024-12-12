import numpy as np

def get_num_right_down(arr: np.array, i, j) -> int:
    smaller_arr: np.array = arr[i:i+3, j:j+3]
    diagonal = "".join(smaller_arr.diagonal())
    inverse_diagonal = "".join(np.rot90(smaller_arr, k=-1).diagonal())
    counter: int = 0
    for s in [diagonal, inverse_diagonal]:
        if s == "MAS":
            counter += 1
        elif s == "SAM":
            counter += 1
    if counter == 2:
        return 1
    else:
        return 0


### main ###

# file = open("src/day-04/example_2.txt")
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


