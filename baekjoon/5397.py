# 키로거
tc = int(input())

for _ in range(tc):
    log = input()
    left_stk, right_stk = [], []
    for ch in log:
        if ch == '-':
            if left_stk:
                left_stk.pop()
        elif ch == '<':
            if left_stk:
                right_stk.append(left_stk.pop())
        elif ch == '>':
            if right_stk:
                left_stk.append(right_stk.pop())
        else:
            left_stk.append(ch)
    left_stk.extend(reversed(right_stk))
    print("".join(left_stk))
