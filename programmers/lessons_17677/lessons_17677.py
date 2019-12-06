from collections import defaultdict


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    union_count, intersection_count = 0, 0
    str1_dict = defaultdict(int)
    str2_dict = defaultdict(int)

    for i in range(len(str1) - 1):
        letters = str1[i: i + 2]
        if letters.isalpha():
            str1_dict[letters] += 1

    for i in range(len(str2) - 1):
        letters = str2[i: i + 2]
        if letters.isalpha():
            str2_dict[letters] += 1

    for k, v in str1_dict.items():
        if k in str2_dict:
            intersection_count += min(v, str2_dict[k])
            union_count += max(v, str2_dict[k])
        else:
            union_count += v

    for k, v in str2_dict.items():
        if k not in str1_dict:
            union_count += v

    if union_count == 0:
        return 65536
    return int(intersection_count / union_count * 65536)


print(solution("handshake", "shake hands"))
