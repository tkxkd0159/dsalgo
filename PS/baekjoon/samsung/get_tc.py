import sys
sys.stdin = open('../test_case/16236.txt', 'r')

N = int(input())
for test_case in range(1, N+1):
    print(f"testcase # {test_case}")
    m_size = int(input())
    fmap = []
    for i in range(m_size):
        fmap.append(list(map(int, input().split())))

    print(m_size)
    print(fmap)
