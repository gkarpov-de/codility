def solution(H):
    prevs = [H[0]]
    count = 1

    for i in range(1, len(H)):
        h = H[i]
        peek = prevs[-1]
        if h < peek:
            while len(prevs) > 0 and prevs[-1] >= h:
                if prevs.pop() == h:
                    count -= 1
                    break

        if h != peek:
            count += 1
            prevs.append(h)

    return count


print(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))
