import heapq as hq


def solution(operations):
    queue = []
    for op in operations:
        letter, num = op.split()
        if letter == 'I':
            hq.heappush(queue, int(num))
        else:
            if num == '1' and queue:
                element = queue.pop()
                if queue and queue[-1] > element:
                    queue.pop()
                    hq.heappush(queue, element)
            elif num == '-1' and queue:
                hq.heappop(queue)

    if not queue:
        return [0, 0]

    minimum = hq.heappop(queue)
    maximum = queue.pop()
    if queue and queue[-1] > maximum:
        maximum = queue.pop()

    return [maximum, minimum]

print(solution(["I 7", "I 5", "I -5", "D -1"]))