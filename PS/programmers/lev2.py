def solution(s):
    answer = []
    cnt_0 = 0
    total_0 = []
    cnt_1 = 0
    iter_ = 0
    while s != "1":
        for i in s:
            if i == "0":
                cnt_0 += 1
            elif i == "1":
                cnt_1 += 1

        total_0.append(cnt_0)

        new_s = ""
        while cnt_1 != 1:
            new_s = str(cnt_1 % 2) + new_s
            cnt_1 = cnt_1 // 2

        s = "1" + new_s
        iter_ += 1
        cnt_0 = 0
        cnt_1 = 0

    answer.append(iter_)
    answer.append(sum(total_0))

    return answer


solution("110010101001")