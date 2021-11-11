def solution(A):
    num_str = ""

    while A > 1:
        quo = A // 2
        rem = A - quo * 2
        A = quo

        num_str = str(rem) + num_str
        if quo == 1:
            num_str = str(quo) + num_str

    init_1_sig = False
    zero_cnt = 0
    gap_cand = []
    for n in num_str:
        if n == "1" and init_1_sig is False:
            init_1_sig = True
        elif n == "0" and init_1_sig is True:
            zero_cnt += 1
        else:
            gap_cand.append(zero_cnt)
            zero_cnt = 0

    if len(gap_cand) == 0:
        return 0

    return max(gap_cand)

print(solution(1041))
print(solution(35))
print(solution(15))