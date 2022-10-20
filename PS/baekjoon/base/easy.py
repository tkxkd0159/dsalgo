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

def solve10814():
    N = int(read().rstrip())
    
    users = []
    cnt = 1
    for i in range(1, 1+N):
        age, name = read().rstrip().split()
        users.append([i, int(age), name])
        cnt+=1
    
    users = sorted(users, key=lambda u: (u[1], u[0]))
    for i, age, name in users:
        print(f'{age} {name}')