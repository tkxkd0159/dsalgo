from typing import List


def merge(nums1: List[int], nums2: List[int], m, n):
    i = m - 1
    j = n - 1
    k = i + j + 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

    if j >= 0:
        nums1[: j + 1] = nums2[: j + 1]

    print(nums1)


merge([4, 5, 6, 0, 0, 0], [1, 2, 3], 3, 3)
