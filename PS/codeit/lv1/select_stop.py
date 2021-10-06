def select_stops(water_stops, capacity):
    pick_stop = []
    start = 0
    end = water_stops[-1]

    if water_stops[0] > capacity:
        return False
    elif water_stops[0] == capacity:
        pick_stop.append(water_stops[0])

    for idx, stop in enumerate(water_stops):
        if stop == end:
            pick_stop.append(stop)
            break
        diff = water_stops[idx] - start
        next_diff = water_stops[idx+1] - start
        if ((diff < capacity) and (next_diff > capacity)) or (diff == capacity):
            pick_stop.append(stop)
            start = stop
        elif diff == capacity:
            pick_stop.append(stop)
            start = stop

    return pick_stop


def select_stops_ans(water_stops, capacity):
    stop_list = []

    # 마지막 들른 약수터 위치
    prev_stop = 0

    for i in range(len(water_stops)):
        # i 지점까지 갈 수 없으면, i - 1 지점 약수터를 들른다
        if water_stops[i] - prev_stop > capacity:
            stop_list.append(water_stops[i - 1])
            prev_stop = water_stops[i - 1]

    stop_list.append(water_stops[-1])

    return stop_list


list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))