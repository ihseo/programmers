from collections import deque


def solution(progresses, speeds):
    answer = []
    days_queue = deque(-((100 - x) // -y) for x, y in zip (progresses, speeds))
    for x in days_queue:
        print(x)

    while days_queue:
        function = days_queue.popleft()
        count = 1
        while days_queue:
            if days_queue[0] <= function:
                days_queue.popleft()
                count += 1
            else:
                break
        answer.append(count)

    return answer

print(solution([93,30,55], [1,30,5]))