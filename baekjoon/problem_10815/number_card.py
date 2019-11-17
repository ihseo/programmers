card_num = int(input())
cards = set(input().split())

testcard_num = int(input())
test_cards = input().split()

answer = ' '.join('1' if c in cards else '0' for c in test_cards)
print(answer)