def solution(genres, plays) -> list:
    my_dict = {e: [] for e in set(genres)}
    for g, p in zip(genres, plays):
        my_dict[g] += [p]
    sorted_list = [(i, g, p) for i, (g, p) in sorted(enumerate(zip(genres, plays)),
                                    key=lambda x: (-sum(my_dict[x[1][0]]), -x[1][1], x[0]))]
    count_dict = {e: 0 for e in set([x[1] for x in sorted_list])}

    answer = []
    for item in sorted_list:
        if count_dict[item[1]] == 2:
            continue
        answer.append(item[0])
        count_dict[item[1]] += 1
    return answer

print(solution(['classic', 'a', 'kill', 'kill', 'kill', 'kill', 'pop', 'classic', 'a', 'classic', 'pop'], [500, 15555, 3550, 3550, 923, 2244, 3, 409, 150, 800, 2500]))