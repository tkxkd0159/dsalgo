from bisect import bisect_right
def sum_in_list(search_sum, sorted_list):  # O(NlogN)
    for elem in sorted_list:
        rem = search_sum - elem
        tgt_idx = bisect_right(sorted_list, rem) - 1
        if rem == sorted_list[tgt_idx]:
            return True

    return False

def sum_in_list(search_sum, sorted_list): # O(N)
    low = 0
    high = len(sorted_list) - 1

    while low < high:
        candidate_sum = sorted_list[low] + sorted_list[high]

        if candidate_sum == search_sum:
            return True

        if candidate_sum < search_sum:
            low += 1

        else:
            high -= 1

    return False

print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))