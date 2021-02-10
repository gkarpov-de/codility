def solution(s):
    stack = list()
    lbr = ['(', '[', '{']
    rbr = [')', ']', '}']
    for c in s:
        if c in lbr:
            stack.append(c)
            continue

        if c in rbr:
            if len(stack) == 0 or rbr.index(c) != lbr.index(stack.pop()):
                return 0

    return 1 if len(stack) == 0 else 0


print(solution("fgdhd{asd[()(34g)dghd]}"))
