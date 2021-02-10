def solution(A):
    # print(f'A: {A}')
    A.sort(reverse=1)

    for i in range(len(A) - 2):
        if A[i] >= A[i + 1] + A[i + 2]:
            continue

        if A[i + 1] < A[i] + A[i + 2] and A[i + 2] < A[i] + A[i + 1]:
            print(A[i], A[i + 1], A[i + 2])
            return 1

    return 0


print(solution([10, 50, 5, 1]))
print(solution([10, 2, 5, 1, 8, 20]))
print(solution([4, 5, 11]))
