def solution(citations):
    answer = 0
    c = sorted(citations)
    h = 0
    out = False
    for i in range(1, 10001):
        check_point = 0
        for j, cite in enumerate(c):
            if h == cite:
                check_point = j
                continue
            elif cite > i and h == i:
                break

            if cite >= i and (len(c[j:]) >= i):
                h = i
                check_point = j
            elif len(c[j:]) < cite:
                out = True
                break
        if out:
            break

        c = c[check_point:]

    answer = h
    return answer