"""
We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:

  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0

  N is an integer within the range [0..100,000];
  each element of array A is an integer within the range [0..2,147,483,647].
"""
# 수평선에 막대기로 범위 표시를 하고 lower tick 마다 겹치는 부분을 센다고 생각

def solution(A):
    lower = []
    upper = []
    for i, elem in enumerate(A):
        lower.append(i-elem)
        upper.append(i+elem)

    lower.sort()
    upper.sort()

    ans = 0
    inter = 0
    upper_cursor = 0

    for l in lower:
        while l > upper[upper_cursor]:
            inter -= 1
            upper_cursor += 1

        ans += inter
        inter += 1
        if ans > 10_000_000:
            return -1

    return ans