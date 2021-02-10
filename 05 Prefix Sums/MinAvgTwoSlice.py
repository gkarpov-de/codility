import PrefixSum

def solution(A):
    min_avg_value = (A[0] + A[1]) / 2.0  # The mininal average
    min_avg_pos = 0  # The begin position of the first
    # slice with mininal average
    for index in range(0, len(A) - 2):
        # Try the next 2-element slice
        if (A[index] + A[index + 1]) / 2.0 < min_avg_value:
            min_avg_value = (A[index] + A[index + 1]) / 2.0
            min_avg_pos = index
        # Try the next 3-element slice
        if (A[index] + A[index + 1] + A[index + 2]) / 3.0 < min_avg_value:
            min_avg_value = (A[index] + A[index + 1] + A[index + 2]) / 3.0
            min_avg_pos = index
    # Try the last 2-element slice
    if (A[-1] + A[-2]) / 2.0 < min_avg_value:
        min_avg_value = (A[-1] + A[-2]) / 2.0
        min_avg_pos = len(A) - 2

    return min_avg_pos


A = [4, 2, 2, 5, 1, 5, 8]

# slice (1, 2), whose average is (2 + 2) / 2 = 2;
# slice (3, 4), whose average is (5 + 1) / 2 = 3;
# slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
# print(avg[0][1])
# print(avg[0][3])
# print(avg[2][1])

print(solution(A))
