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







def main():
    # unsorted_list = [element for element in input().split()]
    sample = Sort([4,2,6,1,9,3])
    print(sample.insertion_sort())





if __name__ == "__main__":
    main()
