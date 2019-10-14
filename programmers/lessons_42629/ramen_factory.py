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
#
# import heapq
#
# def solution(stock, dates, supplies, k):
#     answer = 0
#     day = stock
#     date_supply_list = list(zip(dates, supplies))
#     possible_supply = list()
#
#     while day < k:
#         for idx, (date, supply) in enumerate(date_supply_list):
#             if date <= day:
#                 heapq.heappush(possible_supply, -supply)
#                 idx += 1
#             else:
#                 break
#         date_supply_list = date_supply_list[idx:]
#
#         day += -heapq.heappop(possible_supply)
#         answer += 1
#
#     return answer
# solution(4, [4,10,15], [20,5,10], 30)
