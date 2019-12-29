def clock_number(num):
    clock_num = num
    for _ in range(3):
        num = num % 1000 * 10 + num // 1000
        if num < clock_num:
            clock_num = num
    return clock_num


def solution():
    number = int(''.join(input().split()))
    number = clock_number(number)
    count = 0

    for n in range(1111, 10000):
        if n == clock_number(n):
            count += 1
        if n == number:
            return count


print(solution())