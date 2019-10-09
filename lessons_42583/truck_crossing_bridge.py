from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque()
    truck_weights = deque(truck_weights)
    time_passed, current_weight, DUMMY_TRUCK = 0, 0, 0

    while truck_weights:
        time_passed += 1
        if current_weight + truck_weights[0] <= weight:
            current_weight += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(DUMMY_TRUCK)
        if len(bridge) == bridge_length:
            current_weight -= bridge.popleft()

    return time_passed + bridge_length
solution(2, 10, [7, 4, 5, 6])