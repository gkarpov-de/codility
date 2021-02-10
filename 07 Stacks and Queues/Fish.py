def solution(A, B):
    count = len(A)
    downstream_fishs = []
    for i in range(len(A)):
        if B[i] == 1:
            downstream_fishs.append(i)
        else:
            while len(downstream_fishs) > 0:
                count -= 1
                ds_fish_index = downstream_fishs.pop()
                if A[i] < A[ds_fish_index]:
                    downstream_fishs.append(ds_fish_index)
                    break  # while

    return count


# print(solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))
print(solution([2, 1], [0, 1])) # 1
print(solution([], [])) # 1
