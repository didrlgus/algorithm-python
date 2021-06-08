# 컵라면
import heapq

n = int(input())
arr = []
q = []

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a,b))

arr.sort()

for el in arr:
    dead_line = el[0]
    heapq.heappush(q, el[1])
    if len(q) > dead_line:
        heapq.heappop(q)

print(sum(q))