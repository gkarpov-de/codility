def solution(A, B, K):
    if(A > B or K == 0):
        return 0;

    result = 0 if A > 0 else 1;

    toB = int(B/K)
    toA = int((A-1)/K) if A > 1 else 0
    result += toB-toA

    return result

print(f'solution = {solution(0, 2000000000, 1)}')
