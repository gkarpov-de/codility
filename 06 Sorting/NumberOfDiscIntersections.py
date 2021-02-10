import heapq


def solution(A):
    n = len(A)
    t = []

    opened = {}
    closed = {}
    opcl = {}
    for i in range(n):
        begin = i - A[i]
        end = i + A[i]
        heapq.heappush(t, (begin, i))
        heapq.heappush(t, (end, i))
        opened[begin] = opened.setdefault(begin, 0) + 1
        opened[end] = opened.setdefault(end, 0)
        closed[begin] = closed.setdefault(begin, 0)
        closed[end] = closed.setdefault(end, 0) + 1

    count = 0

    st = set()
    while len(t) > 0:
        if count > 10000000:
            return -1

        x, i = heapq.heappop(t)
        # print(f'{i}: {x} - {st}')
        if i in st:
            st.remove(i)

        else:
            count += len(st)
            st.add(i)

    # print(f'count before update: {count}')
    count += get_touched_intervals(A, opened, closed)

    return count


def get_touched_intervals(A, opened, closed):
    # print(f'opened: {opened}')
    # print(f'closed: {closed}')
    delta = 0
    for i in list(opened):
        opcl = opened[i] * closed[i]
        if opcl > 0:
            isZeroLengthInterval = i in range(len(A)) and A[i] == 0
            # print(f'{i}: {A[i]}/{opcl} <{isZeroLengthInterval}>')
            # if zero length interval
            if isZeroLengthInterval:
                delta += opcl - 1
            else:
                delta += opcl

    # print(f'delta: {delta}')
    return delta


print(solution([1, 5, 2, 1, 4, 0]))  # 11
print(solution([2, 0, 1]))  # 3
print(solution([1, 1, 1]))  # 3
print(solution([1, 0, 1, 0, 1]))  # 6
print(solution([1, 0, 1]))  # 3
