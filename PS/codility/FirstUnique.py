def solution(A):
    unique_s = set()
    dupl_s = set()
    idx_dict = dict()
    for i, elem in enumerate(A):
        if elem in dupl_s:
            continue
        elif elem not in unique_s:
            unique_s.add(elem)
            idx_dict[elem] = i
        else:
            unique_s.remove(elem)
            dupl_s.add(elem)
            del idx_dict[elem]

    if len(unique_s) == 0:
        return -1
    else:
        min_idx = 1e9
        for k, v in idx_dict.items():
            min_idx = min(v, min_idx)

        return A[min_idx]