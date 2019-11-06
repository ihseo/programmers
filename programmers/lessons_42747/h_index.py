def solution(citations):
    index = 0
    citations.sort()
    for i in range(len(citations)):
        number = len(citations) - i
        if min(number, citations[i]) > index:
            index = min(number, citations[i])
    return index
