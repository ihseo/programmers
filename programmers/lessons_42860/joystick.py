def solution(name):
    N = len(name)
    name_list = []
    cursor, count, total = 0, 0, 0
    for letter in name:
        if letter == 'A':
            count += 1
        name_list.append(ord(letter))

    while True:
        if name_list[cursor] != 65:
            total += (name_list[cursor] - 65) if name_list[cursor] - 65 <= 13 else 26 - (name_list[cursor] - 65)
            name_list[cursor] = 65
            count += 1

        if count == N:
            return total

        for i in range(1, (N + 1)):
            if name_list[cursor + i] != 65:
                cursor += i
                total += i
                break
            if name_list[cursor - i] != 65:
                cursor -= i
                total += i
                break

print(solution("AAAAAFAAAB"))