def solution(A):
    A.sort()
    count = 1
    n = len(A)
    lastDistinctNumber = A[0]
    for i in range(1, n):
        if lastDistinctNumber != A[i]:
            lastDistinctNumber = A[i]
            count += 1

    return count


A = [2, 1, 1, 2, 3, 1, 5, 5]
distinctNumbers = set(A)
print(len(distinctNumbers))

print(solution(A))