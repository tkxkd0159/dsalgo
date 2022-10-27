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

def solve9091():
    N = int(read().rstrip())
    def chkPS(strs):
        dq = deque()

        for s in strs:
            if s == "(":
                dq.append(s)
            elif s == ")":
                if len(dq) == 0:
                    return "NO"
                else:
                    dq.pop()
        if len(dq) == 0:
            return "YES"
        else:
            return "NO"
    
    for _ in range(N):
        print(chkPS(read().rstrip()))

def solve10816():
    from collections import Counter
    _ = read()
    C = Counter(read().split())
    _ = read()
    targets = read().split()
    print(' '.join(f'{C[t]}' if t in C else '0' for t in targets))