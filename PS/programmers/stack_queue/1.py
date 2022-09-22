class School:
    def __init__(self) -> None:
        pass

    @staticmethod
    def prob1():
        # https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=python3
        answer = []
        for e in arr:
            if answer[-1:] != [e]:
                answer.append(e)
        return answer


def solution(progresses, speeds):
    answer = []
    final = 100
    days = []
    for i in range(len(progresses)):
        tmp = (final - progresses[i]) // speeds[i]
        r = (final - progresses[i]) % speeds[i]
        if r > 0:
            tmp += 1
        days.append(tmp)

    max_day = 0
    for q in days:
        if q > max_day:
            max_day = q
            answer.append(1)
        else:
            answer[-1] += 1

    return answer


def solution2(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((p-100) // s):
            Q.append([-((p-100) // s), 1])
        else:
            Q[-1][1] += 1
    return [q[1] for q in Q]


def solution3(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses) > 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
