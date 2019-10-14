from collections import deque
def solution(m, n, infests, vaccinateds):
    NORMAL, INFECTED, VACCINATED = 0, 1, 2
    count = -1
    q = deque()
    office = [[0] * n for _ in range(m)]
    for infected in infests:
        office[infected[0] - 1][infected[1] - 1] = INFECTED
        q.append((infected[0]-1, infected[1]-1))
    for vac in vaccinateds:
        office[vac[0] - 1][vac[1] - 1] = VACCINATED
    while q:
        count += 1
        for _ in range(len(q)):
            row, col = q.popleft()
            for row_, col_ in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if 0 <= row_ < m and 0 <= col_ < n and office[row_][col_] == NORMAL:
                    office[row_][col_] = INFECTED
                    q.append((row_, col_))
    for space in office:
        if NORMAL in space:
            return -1
    return count
print(solution(23, 47, [[1,4], [1,5], [2,9], [11, 11]], [[1,7],[2,4]]))