from functools import reduce

def get_minend(a, b):
    if isinstance(a, tuple):
        a = a[1]
    return max(a, b[1])

def sel_recursion(course_ls, my_lecs):
    if len(course_ls) == 0:
        return my_lecs
    else:

        cursor = 0
        min_ = reduce(get_minend, course_ls)
        prev_end = 0 if len(my_lecs) == 0 else my_lecs[-1][1]

        for idx, element in enumerate(course_ls):
            start = element[0]
            end = element[1]
            if start <= prev_end:
                continue
            min_ = min(min_, end)
            if (min_ == end) and (start > prev_end):
                cursor = idx


        if course_ls[cursor][0] > prev_end:
            my_lecs.append(course_ls[cursor])
            course_ls.pop(cursor)
            sel_recursion(course_ls, my_lecs)
        else:
            return my_lecs

    return my_lecs

def course_selection(course_ls):
    my_lectures = []
    return sel_recursion(course_ls, my_lectures)


def course_selection2(course_list):
    sorted_list = sorted(course_list, key=lambda x: x[1])

    # 가장 먼저 끝나는 수업은 무조건 듣는다
    my_selection = [sorted_list[0]]

    # 이미 선택한 수업과 안 겹치는 수업 중 가장 빨리 끝나는 수업을 고른다
    for course in sorted_list:
        if course[0] > my_selection[-1][1]:
            my_selection.append(course)

    return my_selection


# cases :
# 1. 가장 먼저 시작하는 수업 고르기
# 2. 겹치는 수업이 가장 적은 수업부터 고르기
# 3. 가장 짧은 수업부터 고르기
# 4. 가장 먼저 끝나는 수업부터 고르기
if __name__ == "__main__":
    print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
    print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
    print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))