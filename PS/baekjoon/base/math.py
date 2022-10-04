def is_prime(n)-> bool:
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n ** (1/2) + 1):
        if n % i == 0:
            return False
    return True

def solve1978():
    N = int(input())
    primes = list(map(int, input().split()))
    ans = 0
    for p in primes:
        if is_prime(p) == True:
            ans += 1
    print(ans)

