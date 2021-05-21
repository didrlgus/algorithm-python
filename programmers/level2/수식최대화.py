# 수식최대화
import re
from itertools import permutations


def solution(expression):
    answer = -1
    expression = re.split("([-+*]{1})", expression)
    permu_list = list(permutations(["-", "+", "*"], 3))

    for permu in permu_list:
        tmp_exp = expression[:]
        for op in permu:
            while op in tmp_exp:
                idx = tmp_exp.index(op)
                tmp_exp[idx - 1] = str(
                    eval(tmp_exp[idx - 1] + op + tmp_exp[idx + 1])
                )
                del tmp_exp[idx : idx + 2]
        answer = max(answer, abs(int(tmp_exp[0])))
    return answer
