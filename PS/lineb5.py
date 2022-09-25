from collections import deque
from copy import deepcopy


def solution(jobs):
    answer = []
    # start / period / class / priority
    q = deque([jobs[0]])
    rest = deque(jobs[1:])
    end = 1
    endremain = [0] * 11
    endremain[q[0][2]] = q[0][1]
    while q:
        j = q.popleft()
        if answer[-1:] != [j[2]]:
            answer.append(j[2])
        end += j[1]
        endremain[j[2]] -= j[1]

        tmp = []
        resttmp = deepcopy(rest)
        for r in resttmp:
            if r[0] <= end:
                if r[2] == j[2]:
                    q.appendleft(r)
                    rest.popleft()
                    endremain[j[2]] += r[1]
                    continue
                else:
                    tmp.append(rest.popleft())
        pmap = dict()
        for _, tt, c, p in tmp:
            acc = pmap.get(c, [0, 0])
            pmap[c] = [acc[0]+tt, acc[1]+p]
        if endremain[j[2]] == 0:
            for _, tt, c, p in q:
                acc = pmap.get(c, [0, 0])
                pmap[c] = [acc[0]+tt, acc[1]+p]
            tmp.extend(q)
            q = deque()

        cpsort = []
        for c, (tt, p) in pmap.items():
            cpsort.append((c, p))
        cpsort = sorted(
            sorted(cpsort, key=lambda x: x[1], reverse=True), key=lambda x: x[0])

        for c, _ in cpsort:
            for i, elem in enumerate(tmp):
                if elem[2] == c:
                    q.append(tmp[i])
        if endremain[j[2]] == 0:
            if len(q) > 0:
                endremain[q[0][2]] = pmap[q[0][2]][0]

    return answer


print(solution([[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [
    5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]]))  # 2123
