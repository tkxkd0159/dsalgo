"""
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
"""


def solution(N, A):
    counter = [0] * N

    max_num = 0
    for i in A:
        if i > N:
            counter = [max_num] * N  # 맨 처음에는 그냥 max(counter) 해서 풀었는데 O(N^2)으로 시간초과남. 하지만 이것도 마지막 케이스 안됨.
        else:
            counter[i-1] += 1
            max_num = max(max_num, counter[i-1])
    return counter

def answer(N, A):
    counter = [0] * N

    max_num = 0
    max_counter_status = 0
    for i in A:
        if i > N:
            max_counter_status = max_num  # 리스트 업데이트 하기 위해 O(N) 연산 안하고 그냥 업데이트 해야 되는 값을 상태 저장
        else:
            if max_counter_status > counter[i-1]:
                counter[i-1] = max_counter_status + 1
            else:
                counter[i-1] += 1
            max_num = max(max_num, counter[i-1])

    for i in range(len(counter)):
        if counter[i] < max_counter_status:
            counter[i] = max_counter_status
    return counter