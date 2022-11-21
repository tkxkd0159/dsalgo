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

N = int(read())
dots = []
for _ in range(N):
    dots.append(tuple(map(int, read().split())))

sorted_dots = sorted(dots, key=lambda x: (x[1], x[0]))
for d in sorted_dots:
    print(d[0], d[1])