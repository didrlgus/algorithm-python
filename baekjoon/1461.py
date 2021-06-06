# 도서관
import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))

mx = max(max(arr), -min(arr))

left, right = [], []

for el in arr:
    if el < 0:
        heapq.heappush(left, el)
    else:
        heapq.heappush(right, -el)

ret = 0
while left:
    ret += heapq.heappop(left)
    for _ in range(m-1):
        if left:
            heapq.heappop(left)

while right:
    ret += heapq.heappop(right)
    for _ in range(m-1):
        if right:
            heapq.heappop(right)

print(-ret*2-mx)
