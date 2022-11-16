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

a, b, v = map(int, read().split())
q = (v-a) // (a-b)
rem = (v-a) % (a-b)
if rem != 0:
    print(q+2)
else:
    print(q+1)