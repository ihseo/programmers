from itertools import permutations


def does_match(candidate, guess):
    candidate = ''.join(map(str, candidate))
    num, strike, ball = guess
    num = str(num)
    cand_strike = sum(letter1 == letter2 for letter1, letter2 in zip(candidate, num))
    cand_ball = len(set(candidate) & set(num)) - cand_strike
    return (cand_strike, cand_ball) == (strike, ball)

    if (cand_strike, cand_ball) == (strike, ball):
        return True
    return False


def solution(baseball):
    candidates = set()
    count = 0
    for r in permutations(range(1, 10), 3):
        candidates.add(r)
    for cand in candidates:
        if all(does_match(cand, guess) for guess in baseball):
            count += 1

    return count


print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))
