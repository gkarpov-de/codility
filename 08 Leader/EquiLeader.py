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


def solution(a):
    equi_leaders = 0
    n = len(a)
    index = leader_index(a)
    if index < 0:
        return 0

    leader = a[index]
    total_count = a.count(leader)

    if total_count <= len(a) >> 1:
        return 0

    c1 = 0
    for i in range(n):
        if a[i] == leader:
            c1 += 1

        c2 = total_count - c1
        if (i + 1) >> 1 < c1 and (n - i - 1) >> 1 < c2:
            equi_leaders += 1

    return equi_leaders


print(solution([4, 3, 4, 4, 4, 2]))
