def solution(A):
    numOf0 = 0
    for i in A:
        if i == 0:
            numOf0 +=1

    n = len(A)
    numOf1 = len(A) - numOf0
    arr = []
    for i in range(n):
        if A[i] == 0:
            arr.append(numOf1)
            numOf0 -= 1
        else:
            numOf1 -= 1

    return sum(arr)

A = [0, 1, 0, 1, 1]
print(solution(A))