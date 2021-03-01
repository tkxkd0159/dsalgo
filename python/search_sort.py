class Search:

    def __init__(self, lists):
        self.lists = lists

    def linear_search(self, target):
        idx = 0
        for element in self.lists:
            if target == element:
                return idx
            idx += 1

        return None

    def binary_search(self, target):
        start_index = 0
        end_index = len(self.lists) - 1

        while start_index <= end_index:
            midpoint = (start_index + end_index) // 2
            if self.lists[midpoint] == target:
                return midpoint
            elif self.lists[midpoint] > target:
                end_index = midpoint - 1
            else:
                start_index = midpoint + 1
        return None

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
            for cf_idx in range(idx+1, scan_range):
                if self.lists[cf_idx] < min_num:
                    min_num = self.lists[cf_idx]
                    min_num_idx = cf_idx

            if min_num_idx != idx:
                temp = self.lists[idx]
                self.lists[idx] = min_num
                self.lists[min_num_idx] = temp

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
            i = start_idx # scan index
            b = start_idx # big group index
            p = end_idx   # pivot index

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




if __name__ == "__main__":
    main()
