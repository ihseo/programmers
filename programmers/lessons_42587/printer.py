from collections import deque


def solution(priorities, location):
    order = 0
    sorted_list = sorted(priorities)
    priorities_queue = deque([(i, p) for i, p in enumerate(priorities)])
    while priorities_queue:
        index, task = priorities_queue.popleft()
        if task == sorted_list[-1]:
            order += 1
            if index == location:
                return order
            sorted_list.pop()
        else:
            priorities_queue.append((index, task))