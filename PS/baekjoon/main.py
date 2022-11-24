from copy import deepcopy
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
from datetime import datetime
from math import factorial
from base import *


# BruteForce.solve1018()



# from base.easy import solve9091
# solve9091()

import sys
read = sys.stdin.readline

K, N = map(int, read().split())
l = []
for _ in range(K):
    l.append(int(read()))

low = 1
high = max(l)
cached = 0

while low <= high:
    mid = (low + high) // 2
    tot = 0
    for elem in l:
        tot += (elem // mid)
    
    if tot >= N:
        cached = mid
        low = mid + 1
    else:
        high = mid - 1
print(cached)
