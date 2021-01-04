from math import sqrt


def max_product(left_cards, right_cards):
    product_list = []
    for left in left_cards:
        for right in right_cards:
            product_list.append(left*right)
    
    return max(product_list)




# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    def distance(store1, store2):
        return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

    min_dis = distance(coordinates[0], coordinates[1])

    for store1_idx in range(len(coordinates) - 1):
        for store2_idx in range(store1_idx + 1, len(coordinates)):
            if distance(coordinates[store1_idx], coordinates[store2_idx]) < min_dis:
                min_dis = distance(coordinates[store1_idx], coordinates[store2_idx])
                pair = [coordinates[store1_idx], coordinates[store2_idx]]

    return pair

def trapping_rain(buildings):
    total_rain = 0
    max_height = max(buildings)
    target_idx = 0
    current_idx = 0

    while current_idx < len(buildings) - 2:
        target = buildings[target_idx]
        if buildings[current_idx] == max_height:
            target = max(buildings[target_idx+1:])
            max_height = target
        for compare_idx in range(target_idx + 1, len(buildings) - 1):
            if target - buildings[compare_idx] >= 0:
                total_rain += target - buildings[compare_idx]
                current_idx = compare_idx
            else:
                target_idx = compare_idx
                current_idx = compare_idx
                break


    return total_rain

def trapping_rain2(buildings):
    # 총 담기는 빗물의 양을 변수에 저장
    total_height = 0

    # 리스트의 각 인덱스을 돌면서 해당 칸에 담기는 빗물의 양을 구한다
    # 0번 인덱스와 마지막 인덱스는 볼 필요 없다
    for i in range(1, len(buildings) - 1):
        # 현재 인덱스를 기준으로 양쪽에 가장 높은 건물의 위치를 구한다
        max_left = max(buildings[:i])
        max_right = max(buildings[i:])

        # 현재 인덱스에 빗물이 담길 수 있는 높이
        upper_bound = min(max_left, max_right)

        # 현재 인덱스에 담기는 빗물의 양을 계산
        # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
        total_height += max(0, upper_bound - buildings[i])

    return total_height


if __name__ == "__main__":
    print(max_product([1, 6, 5], [4, 2, 3]))
    test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    print(closest_pair(test_coordinates))
    print(trapping_rain([3, 0, 0, 2, 0, 4]))
    print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
