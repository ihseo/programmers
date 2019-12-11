def solution(record):
    ENTER, LEAVE = 0, 1
    name_dict = dict()
    result = []

    for rec in record:
        rec = rec.split()
        if rec[0] == "Enter":
            name_dict[rec[1]] = rec[2]
            result.append((ENTER, rec[1], "{}님이 들어왔습니다."))
        elif rec[0] == "Leave":
            result.append((LEAVE, rec[1], "{}님이 나갔습니다."))

        elif rec[0] == "Change":
            name_dict[rec[1]] = rec[2]

        print(result)
        print(name_dict)

    answer = [x[2].format(name_dict[x[1]]) for x in result]
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))