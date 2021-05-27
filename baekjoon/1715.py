# 카드 정렬하기
import heapq

n = int(input())
heap = []

for _ in range(n):
    heapq.heappush(heap, int(input()))

ret = 0

while len(heap) > 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum = one + two
    ret += sum
    heapq.heappush(heap, sum)

print(ret)