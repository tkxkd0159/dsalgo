import string
def solution(S):


    index = {c:[-1, -1] for c in string.ascii_uppercase}

    res = 0

    # 두번쨰 이상 등장할 때 그 앞에 나온 위치를 중심으로 좌우 substring의 unique char 계산
    for now, c in enumerate(S):
        first, second = index[c]
        res += (now - second) * (second - first)
        index[c] = [second, now]   # 한번씩 등장할 때마다 index 하나씩 밀림

    # 각 문자별 인덱스로 가장 마지막에 나온 두 곳의 위치만 저장되어 있음.
    # 앞에 루프가 그 앞에 나온 위치를 중심으로 계산한 것이므로 이번에는 최종 위치의 좌우로 unique char 계산
    for c in index:
        first, second = index[c]

        # second를 기준으로 앞은 first까지 뒤로는 끝까지 해당 글자가 없다
        # second 위치를 중심으로 좌우 substring의 unique char 계산
        res += (len(S) - second) * (second - first)

    return res

print("ANSWER : ", solution("AVAX"))