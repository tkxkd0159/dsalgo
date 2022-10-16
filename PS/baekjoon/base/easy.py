from collections import deque
import sys
read = sys.stdin.readline


def solve2164():
    N = int(input())
    cards = deque(range(1, N+1))
    while len(cards) > 1:
        cards.popleft()
        cards.append(cards.popleft())
    print(cards.pop())

def solve10866():
    N = int(read())
    dq = deque()
    for _ in range(N):
        target = read().split()

        if target[0] == "push_front":
            dq.appendleft(int(target[1]))
        elif target[0] == "push_back":
            dq.append(int(target[1]))
        elif target[0] == "pop_front":
            if len(dq) == 0:
                print(-1)
            else:
                print(dq.popleft())
        elif target[0] == "pop_back":
            if len(dq) == 0:
                print(-1)
            else:
                print(dq.pop())
        elif target[0] == "size":
            print(len(dq))
        elif target[0] == "empty":
            if len(dq) == 0:
                print(1)
            else:
                print(0)
        elif target[0] == "front":
            if len(dq) == 0:
                print(-1)
            else:
                print(dq[0])
        elif target[0] == "back":
            if len(dq) == 0:
                print(-1)
            else:
                print(dq[-1])