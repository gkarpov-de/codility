import math

def fillST(S):
    n = len(S)
    st = [[0 for i in range(n)] for j in range(n)]

    for i in range(0, n):
        st[i][0] = S[i]

    j = 1
    while (1 << j) <= n:  # rows
        i = 0
        while (i + (1 << j) - 1) < n:
            if st[i][j - 1] <= st[i + (1 << (j - 1))][j - 1]:
                st[i][j] = st[i][j - 1]
            else:
                st[i][j] = st[i + (1 << (j - 1))][j - 1]
            i += 1
        j += 1

    return st


def getMinWithin(S, p, q):
    j = int(math.log2(q - p + 1))
    st = fillST(S)
    if st[p][j] <= st[q - (1 << j) + 1][j]:
        return st[p][j]
    else:
        return st[q - (1 << j) + 1][j]


def getImpactsList(S):
    impacts = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    return [impacts[c] for c in S]

a = [7, 2, 3, 0, 5, 10, 3, 12, 18]
print(getMinWithin(a, 0, 4))
print(getMinWithin(a, 4, 7))
print(getMinWithin(a, 7, 8))

S = 'CAGCCTA'
print(getImpactsList(S))
P = [2, 5, 0]
Q = [4, 5, 6]

def solution(S, P, Q):
    n = len(P)
    ret = [0] * n
    for i in range(0, n):
        ret[i] =getMinWithin(getImpactsList(S), P[i], Q[i])
    return ret

print(solution(S, P, Q))

def solution2(S, P, Q):
    res = []
    for i in range(len(P)):
        if 'A' in S[P[i]:Q[i]+1]:
            res[i] = 1
        elif 'C' in S[P[i]:Q[i]+1]:
            res[i] = 2
        elif 'G' in S[P[i]:Q[i]+1]:
            res[i] = 3
        else:
            res[i] = 4
    return res

print(solution2(S, P, Q))
