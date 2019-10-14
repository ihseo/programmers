def solution():
    max_rows, max_cols, row, col, N = map(int, input().split(' '))
    hori_dice = [0, 0, 0, 0]
    verti_dice = [0, 0, 0, 0]
    CENTER = 1
    direction_dict = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
    board = [[[0]] for _ in range(max_rows)]
    for i in range(max_rows):
        col_list = list(map(int, input().split(' ')))
        for j in range(max_cols):
            board[i] = col_list
    commands = map(int, input().split())
    for command in commands:
        x, y = direction_dict[command]
        if 0 <= row + x <= max_rows - 1 and 0 <= col + y <= max_cols - 1:
            row += x
            col += y
            if command == 1:
                hori_dice[2], hori_dice[3] = hori_dice[3], hori_dice[2]
                hori_dice[CENTER], hori_dice[2] = hori_dice[2], hori_dice[CENTER]
                hori_dice[0], hori_dice[CENTER] = hori_dice[CENTER], hori_dice[0]
                verti_dice[CENTER] = hori_dice[CENTER]
                verti_dice[CENTER + 2] = hori_dice[CENTER + 2]
            elif command == 2:
                hori_dice[0], hori_dice[CENTER] = hori_dice[CENTER], hori_dice[0]
                hori_dice[CENTER], hori_dice[2] = hori_dice[2], hori_dice[CENTER]
                hori_dice[2], hori_dice[3] = hori_dice[3], hori_dice[2]
                verti_dice[CENTER] = hori_dice[CENTER]
                verti_dice[CENTER + 2] = hori_dice[CENTER + 2]
            elif command == 3:
                verti_dice[0], verti_dice[CENTER] = verti_dice[CENTER], verti_dice[0]
                verti_dice[CENTER], verti_dice[2] = verti_dice[2], verti_dice[CENTER]
                verti_dice[2], verti_dice[3] = verti_dice[3], verti_dice[2]
                hori_dice[CENTER] = verti_dice[CENTER]
                hori_dice[CENTER + 2] = verti_dice[CENTER + 2]
            else:
                verti_dice[2], verti_dice[3] = verti_dice[3], verti_dice[2]
                verti_dice[CENTER], verti_dice[2] = verti_dice[2], verti_dice[CENTER]
                verti_dice[0], verti_dice[CENTER] = verti_dice[CENTER], verti_dice[0]
                hori_dice[CENTER] = verti_dice[CENTER]
                hori_dice[CENTER + 2] = verti_dice[CENTER + 2]
            if board[row][col] == 0:
                board[row][col] = verti_dice[CENTER + 2]
            else:
                verti_dice[CENTER + 2] = board[row][col]
                hori_dice[CENTER + 2] = board[row][col]
                board[row][col] = 0
            print(hori_dice[CENTER])


solution()