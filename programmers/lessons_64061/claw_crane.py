def solution(board, moves):
    N = len(board)
    count = 0
    basket = []
    for move in moves:
        for i in range(N):
            if board[i][move - 1]:
                num = board[i][move - 1]
                board[i][move - 1] = 0
                if basket and basket[-1] == num:
                    basket.pop()
                    count += 2
                else:
                    basket.append(num)
                break

    return count