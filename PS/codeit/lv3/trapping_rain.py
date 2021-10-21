def trapping_rain(buildings):
    b_len = len(buildings)
    left_high = [0 for _ in range(b_len)]
    right_high = [0 for _ in range(b_len)]

    left_high[0] = buildings[0]
    right_high[-1] = buildings[-1]
    for i in range(1, b_len):
        left_high[i] = max(left_high[i-1], buildings[i])
        right_high[b_len-i-1] = max(right_high[b_len-i], buildings[b_len-i-1])

    water = 0
    for i in range(b_len):
        water_i = min(left_high[i], right_high[i]) - buildings[i]
        if water_i > 0:
            water += water_i

    return water


print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
