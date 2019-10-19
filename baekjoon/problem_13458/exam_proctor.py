from math import ceil


def solution():
    test_site = int(input())
    test_takers = map(int, input().split())
    proctor, proctor_assist = map(int, input().split())
    total = test_site

    for site in test_takers:
        site -= proctor
        if site > 0:
            total += ceil(site / proctor_assist)
    return total

print(solution())