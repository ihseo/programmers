from itertools import permutations


def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for d in range(5, num ** (1/2) + 1, 6):
        if num % d == 0 or num % (d + 2) == 0:
            return False
    return True


def solution(numbers):
    num_set = set()
    count = 0
    for i in range(1, len(numbers) + 1):
        for perm in map(''.join, permutations(numbers, i)):
            num_set.add(int(perm))

    for num in num_set:
        count += is_prime(num)
    return count


print(solution("011"))