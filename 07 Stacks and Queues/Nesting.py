def solution(s):
    stack = list()
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return 0

    return 1 if len(stack) == 0 else 0

print(solution("(()(())())"))