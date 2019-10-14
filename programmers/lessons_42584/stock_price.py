def solution(prices):
    ans = []
    for i in range(len(prices)):
        value = 0
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                value += 1
            else:
                value += 1
                break
        ans.append(value)
    return ans
solution([1, 2, 3, 2, 3])