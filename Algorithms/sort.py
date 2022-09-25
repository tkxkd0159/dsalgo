class Sort:
    """The Class of Sorts
    """

    def __init__(self, lists):
        self.lists = lists

    def selection_sort(self):

        scan_range = len(self.lists)
        for idx in range(scan_range):
            min_num = self.lists[idx]
            min_num_idx = idx
            for cf_idx in range(idx + 1, scan_range):
                if self.lists[cf_idx] < min_num:
                    min_num = self.lists[cf_idx]
                    min_num_idx = cf_idx

            if min_num_idx != idx:
                temp = self.lists[idx]
                self.lists[idx] = min_num
                self.lists[
                    min_num_idx] = temp  # self.lists[idx], self.lists[min_num_idx] = self.lists[min_num_idx], self.lists[idx]

        return self.lists

    def insertion_sort(self):

        for key_idx in range(1, len(self.lists)):
            key = self.lists[key_idx]
            cf_idx = key_idx - 1

            while cf_idx >= 0 and self.lists[cf_idx] > key:
                self.lists[cf_idx + 1] = self.lists[cf_idx]
                cf_idx -= 1

            self.lists[cf_idx + 1] = key
        return self.lists

    def merge_sort(self):
        def merge(list1, list2):
            merged_list = []

            while len(list1) > 0 and len(list2) > 0:
                if list1[0] < list2[0]:
                    merged_list.append(list1[0])
                    list1.pop(0)
                else:
                    merged_list.append(list2[0])
                    list2.pop(0)

            if len(list1) != 0:
                merged_list += list1
            elif len(list2) != 0:
                merged_list += list2

            return merged_list

        if len(self.lists) < 2:
            return self.lists

        mid = len(self.lists) // 2
        left_half = self.lists[:mid]
        right_half = self.lists[mid:]

        return merge(Sort(left_half).merge_sort(), Sort(right_half).merge_sort())

    def quick_sort(self, start=0, end=None):
        def swap_elements(my_list, index1, index2):
            temp = my_list[index1]
            my_list[index1] = my_list[index2]
            my_list[index2] = temp

        def partition(my_list, start_idx, end_idx):
            i = start_idx  # scan index
            b = start_idx  # big group index
            p = end_idx  # pivot index

            while i < p:
                if my_list[i] <= my_list[p]:
                    swap_elements(my_list, i, b)
                    b += 1
                i += 1

            swap_elements(my_list, b, p)
            p = b
            return p

        if end == None:
            end = len(self.lists) - 1

        if end - start < 1:
            return
        else:
            p = partition(self.lists, start, end)
            self.quick_sort(start, p - 1)
            self.quick_sort(p + 1, end)


def main():
    # unsorted_list = [element for element in input().split()]
    sample = Sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4])
    sample2 = Sort([28, 13, 9, 30, 1, 48, 5, 7, 15])
    sample.quick_sort()
    print(sample.lists)
    print(sample2.merge_sort())


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


BOOK = True

if __name__ == "__main__":
    if BOOK:
        # top_down()
        # score_top_down()
        find_element()
    else:
        main()
