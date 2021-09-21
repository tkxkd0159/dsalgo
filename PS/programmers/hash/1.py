def solution(participant, completion):
    p_ls = {}
    for p in participant:
        if p_ls.get(p):
            p_ls[p] += 1
        else:
            p_ls[p] = 1
    for c in completion:
        if p_ls[c]:
            p_ls[c] -= 1
    for person, i in p_ls.items():
        if i > 0:
            return person


import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
