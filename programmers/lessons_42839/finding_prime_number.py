from itertools import permutations


def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def solution(numbers):
    num_set = set()
    count = 0
    for i in range(1, len(numbers) + 1):
        for perm in map(''.join, permutations(numbers, i)):
            num_set.add(int(perm))

    for num in num_set:
        if is_prime(num):
            count += 1
    return count

print(solution("011"))