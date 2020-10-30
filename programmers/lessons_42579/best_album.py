def solution(genres, plays) -> list:
    answer, sorted_list = [], []
    count_dict = dict()
    songs_dict = {e: [] for e in set(genres)}

    for g, p, i in zip(genres, plays, range(len(genres))):
        count_dict[g] = count_dict.get(g, 0) + p
        songs_dict[g] += [(i, p)]

    genres_sorted = sorted(count_dict.keys(), key=lambda x: -count_dict[x])
    for genre in genres_sorted:
        sorted_list = sorted(songs_dict[genre], key=lambda x: (-x[1], x[0]))
        answer.extend([i for i, p in sorted_list][:2])

    return answer

print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]))