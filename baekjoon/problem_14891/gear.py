def rotate(s, direction):
    if direction == CLOCK:
        return s[-1] + s[0:-1]
    return s[1:] + s[0]


N, S = 0, 1
CLOCK, COUNTER_CLOCK = 1, -1
gears = [0] * 4
for i in range(4):
    gears[i] = input()

rotate_n = int(input())
rotations = [0] * rotate_n

for i in range(rotate_n):
    rotations[i] = list(map(int, input().split()))

for index, direction in rotations:
    index_ = index - 1
    rotates = []
    original_index = index_
    original_direction = direction

    while index_ < 3 and gears[index_][2] != gears[index_ + 1][6]:
        direction = -direction
        rotates.append([index_ + 1, direction])
        index_ += 1

    index_ = original_index
    direction = original_direction

    while index_ > 0 and gears[index_][6] != gears[index_ - 1][2]:
        direction = -direction
        rotates.append([index_ - 1, direction])
        index_ -= 1

    rotates.append([original_index, original_direction])
    for ind, direc in rotates:
        gears[ind] = rotate(gears[ind], direc)

score = 0
for i, gear in enumerate(gears):
    if int(gear[0]) == S:
        if i == 0:
            score += 1
        elif i == 1:
            score += 2
        elif i == 2:
            score += 4
        else:
            score += 8

print(score)