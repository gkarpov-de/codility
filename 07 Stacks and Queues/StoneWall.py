def solution(H):
    prevs = []
    count = 0
    for h in H:
        if len(prevs) == 0:
            prevs.append(h)
            count += 1
        else:
            last_prev = prevs[-1]
            if h < last_prev:
                count += 1
                while len(prevs) > 0:
                    if prevs[-1] == h:
                        count -= 1
                        prevs.pop()
                        break
                    elif prevs[-1] < h:
                        break
                    else:
                        prevs.pop()

                prevs.append(h)
            elif h == last_prev:
                continue
            elif h > last_prev:
                count += 1
                prevs.append(h)


    return count


print(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))
