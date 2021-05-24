# 외벽점검
from itertools import permutations


def solution(n, weak, dist):
    answer = len(dist) + 1
    len_ = len(weak)

    for i in range(len_):
        weak.append(weak[i] + n)

    for start in range(len_):
        for dist_permu in list(permutations(dist, len(dist))):
            cnt = 1
            cur = weak[start] + dist_permu[0]
            for idx in range(start + 1, start + len_):
                if cur < weak[idx]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    cur = weak[idx] + dist_permu[cnt - 1]
            answer = min(answer, cnt)

    if answer > len(dist):
        return -1

    return answer