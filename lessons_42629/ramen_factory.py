import heapq as hq
def solution(stock, dates, supplies, k):
    count, idx = 0, 0
    queue = []
    while stock < k:
        for i in range(idx, len(dates)):
            if dates[i] <= stock:
                hq.heappush(queue, -supplies[i])
                idx = i + 1
            else:
                break
        stock += -hq.heappop(queue)
        count += 1
    return count
solution(4, [4,10,15], [20,5,10], 30)
