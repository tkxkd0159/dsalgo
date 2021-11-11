# If you just add number simply, the code is timed out. Try "divide"
import time
def solution(X, Y, D):
    if X >= Y:
        return 0

    quo = (Y-X) // D
    rem = (Y-X) % D
    if rem != 0:
        quo += 1

    return quo

start = time.time()

print(solution(1, 1_000_000_000, 3))
print(solution(2, 2, 1))
print(solution(3, 231, 12))

print(time.time() - start)