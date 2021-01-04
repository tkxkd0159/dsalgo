# pylint: disable=invalid-name
# 함수를 사용할 때 원래 위치로 돌아갈 수 있게 callstack에 저장
# callstack 너무 많이 쌓이면 StackOverFlowError로 프로그램 중단됨
# 상황에 따라 재귀 함수, 반복문 중 적절한 것 선택

def countdown(n):
    if n > 0:
        print(n)
        countdown(n - 1)

def factorial(n):
    if n == 1:
        return 1
    if n > 1:
        return n * factorial(n-1)

def fibo(n):

    if n < 3:
        return 1

    return fibo(n - 1) + fibo(n - 2)

def triangle_number(n):

    if n == 1:
        return 1
    elif n < 1:
        return None

    return n + triangle_number(n - 1)

def sum_digits(n):

    if n < 10:
        return n

    return n % 10 + sum_digits(n // 10)

def flip(lists):

    if len(lists) == 0 or len(lists) == 1:
        return lists

    return lists[-1:] + flip(lists[:-1])

def binary_search(element, some_list, start_index=0, end_index=None):
    if end_index is None:
        end_index = len(some_list) - 1

    if start_index > end_index:
        return None

    midpoint = (start_index + end_index) // 2

    if some_list[midpoint] == element:
        return midpoint
    elif some_list[midpoint] > element:
        return binary_search(element, some_list, start_index, midpoint - 1)
    elif some_list[midpoint] < element:
        return binary_search(element, some_list, midpoint + 1, end_index)

def hanoi(num_disks, start_peg, end_peg):
    def move_disk(disk_num, start_peg, end_peg):
        print(f"{disk_num}번 원판을 {start_peg}번 기둥에서 {end_peg}번 기둥으로 이동")

    if num_disks == 0:
        return
    else:
        other_peg = 6 - start_peg - end_peg
        hanoi(num_disks -1, start_peg, other_peg)
        move_disk(num_disks, start_peg, end_peg)
        hanoi(num_disks -1, other_peg, end_peg)

if __name__ == "__main__":
    hanoi(3,1,3)
    print(fibo(10))
