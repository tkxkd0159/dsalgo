###

def top_down():
    n = int(input())
    arr = []
    while True:
        tmp = input()
        if tmp == "":
            break
        else:
            arr.append(tmp)

    arr.sort(reverse=True)
    for i in arr:
        print(i, end=" ")
    print("")


def score_top_down():
    n = int(input())
    arr = []
    for i in range(n):
        name, score = input().split()
        arr.append((name, int(score)))

    arr.sort(key=lambda student: student[1])
    for name, _ in arr:
        print(f'{name}', end=" ")


def find_element():
    def bin_search(arr, target, start, end):
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                start = mid + 1
            elif arr[mid] > target:
                end = mid - 1
        return None

    n, m = 5, 3  # 매장의 부품 개수 / 손님이 요청한 부품 개수
    elem_ls = [8, 3, 7, 9, 2]
    elem_ls.sort()
    client_elem = [5, 7, 9]
    for elem in client_elem:
        if bin_search(elem_ls, elem, 0, len(elem_ls)-1):
            print("yes", end=" ")
        else:
            print("no", end=" ")
