from collections import deque

def solve2164():
    N = int(input())
    cards = deque(range(1, N+1))
    while len(cards) > 1:
        cards.popleft()
        cards.append(cards.popleft())
    print(cards.pop())
