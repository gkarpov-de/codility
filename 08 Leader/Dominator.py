from typing import List


def leader_index(a: List[int]) -> int:
    size = 0
    index = -1
    n = len(a)
    for i in range(n):
        if size == 0:
            index = i
            size += 1
        else:
            if a[index] != a[i]:
                size -= 1
            else:
                size += 1

    return index


def dominator_solution(a: List[int]) -> int:
    index = leader_index(a)
    if index < 0:
        return index

    count = a.count(a[index])

    if count > len(a) // 2:
        return index
    else:
        return -1


print(dominator_solution([2, 3, 4, 3, 2, 3, -1, 3, 3]))
