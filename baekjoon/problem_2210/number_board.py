def search(x, y, num):
    if len(num) == 6:
        num_set.add(num)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= 4 and 0 <= ny <= 4:
            search(nx, ny, num + board[nx][ny])


board = [input().split() for _ in range(5)]
num_set = set()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for x in range(5):
    for y in range(5):
        search(x, y, board[x][y])

print(len(num_set))
