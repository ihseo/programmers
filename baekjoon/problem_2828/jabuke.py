def solution():
    total_cols, size = map(int, input().split())
    current, total = size, 0
    count = int(input())

    for _ in range(count):
        position = int(input())
        if (current - size + 1) <= position <= current:
            total += 0

        elif position < (current - size + 1):
            total += (current - size + 1) - position
            current -= (current - size + 1) - position

        elif position > current:
            total += position - current
            current += position - current
    return total


print(solution())
