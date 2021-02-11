def solution(A):
    size = 0
    for x in A:
        if size == 0:
            value = x
            size += 1
        else:
            if value != x:
                size -= 1
            else:
                size += 1

    count = 0
    index = -1
    for i in range(len(A)):
        if A[i] == value:
            count += 1
            if index < 0:
                index = i

    if count > len(A) // 2:
        return index
    else:
        return -1


print(solution([2, 3, 4, 3, 2, 3, -1, 3, 3]))
