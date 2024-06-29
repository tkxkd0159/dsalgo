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
