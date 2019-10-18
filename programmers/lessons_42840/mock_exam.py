def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score_dict = dict()
    for i in range(1, 4):
        score_dict[i] = 0
    for i, ans in enumerate(answers):
        if pattern1[i % len(pattern1)] == ans:
            score_dict[1] += 1
        if pattern2[i % len(pattern2)] == ans:
            score_dict[2] += 1
        if pattern3[i % len(pattern3)] == ans:
            score_dict[3] += 1
    max_value = max(score_dict.values())

    return sorted([key for key, value in score_dict.items() if value == max_value])


print(solution([1, 2, 3, 4, 5]))