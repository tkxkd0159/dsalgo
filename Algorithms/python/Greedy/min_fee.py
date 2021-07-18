def min_fee(print_page_list):
    sum_ = 0
    prev = 0
    for i in sorted(print_page_list):
        sum_ += (prev + i)
        prev += i

    return sum_

if __name__ == "__main__":
    print(min_fee([6, 11, 4, 1]))
    print(min_fee([3, 2, 1]))
    print(min_fee([3, 1, 4, 3, 2]))
    print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
