def solution(prices):
    records = [x for x in range(len(prices) - 1, -1, -1)]
    for i, price in enumerate(prices):
        for j in range(i + 1, len(prices)):
            if price > prices[j]:
                records[i] = j - i
                break
    return records


print(solution([1, 2, 3, 2, 3]))