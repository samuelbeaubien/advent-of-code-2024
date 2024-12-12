
file = open("src/day-01/input.txt")
lines = file.readlines()
left = []
right = []
for line in lines:
    line = line.strip()
    l, r = line.split("   ")
    left.append(l)
    right.append(r)
left.sort()
right.sort()
distance = 0
for l, r in zip(left, right):
    distance += abs(int(l) - int(r))

right_dict = {}
for r in right:
    if r in right_dict:
        right_dict[r] = right_dict[r] + 1
    else:
        right_dict[r] = 1

total = 0
for l in left:
    if l in right_dict:
        total += int(l) * right_dict[l]


 




print("hello")
