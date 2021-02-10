def solution(A):
    A.sort()
    sum1 = A[-3] * A[-2] * A[-1]
    sum2 = A[-2] * A[-1] * A[0]
    sum3 = A[-1] * A[0] * A[1]
    sum4 = A[0] * A[1] * A[2]

    return max(sum1, sum2, sum3, sum4)


A = [-3, 1, 2, -2, 5, 6]
print(solution(A))
