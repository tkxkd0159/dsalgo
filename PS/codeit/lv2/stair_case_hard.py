# 총 계단 수 / 한번에 올라갈 수 있는 계단 수의 집합
def staircase(stairs, possible_steps):
    stair_tabu = [1, 1]

    for height in range(2, stairs + 1):
        stair_tabu.append(0)

        for step in possible_steps:
            if height - step >= 0:
                stair_tabu[height] += stair_tabu[height - step]

    return stair_tabu[stairs]

print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))