def adventureGuild(n, people):  # p311
    p = sorted(people)
    res = 0
    cnt = 0
    for i in p:
        cnt += 1
        if cnt >= i:
            res += 1
            cnt = 0
    return res


if __name__ == "__main__":
    print(adventureGuild(5, [2, 3, 1, 2, 2]))