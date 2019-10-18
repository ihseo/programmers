def solution():
    comp_number = int(input())
    conn_number = int(input())
    connections = [tuple(map(int, input().split(' '))) for _ in range(conn_number)]
    computers = [1] * comp_number
    queue = {1}
    count = 0

    while queue:
        comp = queue.pop()
        computers[comp - 1] = 0
        count += 1
        for conn1, conn2 in connections:
            if comp == conn1 and computers[conn2 - 1] == 1:
                queue.add(conn2)
            elif comp == conn2 and computers[conn1 - 1] == 1:
                queue.add(conn1)
    return count - 1
print(solution())