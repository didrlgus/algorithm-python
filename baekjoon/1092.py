# 배
import sys

n = int(input())
cranes = list(map(int, input().split()))

m = int(input())
boxes = list(map(int, input().split()))

if max(cranes) < max(boxes):
    print(-1)
    sys.exit()

pos = [0] * n
checked = [False] * m

cranes.sort(reverse=True)
boxes.sort(reverse=True)

ret = 0
cnt = 0

while True:
    if cnt == len(boxes):
        break
    for i in range(n):
        while pos[i] < len(boxes):
            if not checked[pos[i]] and cranes[i] >= boxes[pos[i]]:
                checked[pos[i]] = True
                pos[i] += 1
                cnt += 1
                break
            pos[i] += 1
    ret += 1

print(ret)