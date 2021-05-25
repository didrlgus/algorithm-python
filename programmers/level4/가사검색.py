# 가사검색
from bisect import bisect_left, bisect_right

array = [[] for _ in range(10001)]
r_array = [[] for _ in range(10001)]


def count(arr, left_str, right_str):
    l_idx = bisect_left(arr, left_str)
    r_idx = bisect_right(arr, right_str)

    return r_idx - l_idx


def solution(words, queries):
    answer = []

    for word in words:
        array[len(word)].append(word)
        r_array[len(word)].append(word[::-1])

    for i in range(1, 10001):
        array[i].sort()
        r_array[i].sort()

    for query in queries:
        if query[0] != "?":
            ret = count(array[len(query)], query.replace("?", "a"), query.replace("?", "z"))
        else:
            ret = count(
                r_array[len(query)],
                query[::-1].replace("?", "a"),
                query[::-1].replace("?", "z"),
            )

        answer.append(ret)

    return answer