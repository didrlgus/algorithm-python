# 효율적인 해킹

from collections import deque

def bfs(start):
    visited = [False] * (n+1)
    q = deque([start])
    visited[start]=True
    count = 1
    while q:
        front = q.popleft()
        for next in adj[front]:
            if not(visited[next]):
                visited[next]=True
                q.append(next)
                count += 1
    return count

n, m = map(int, input().split(" "))

adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split(" "))
    adj[b].append(a)

MAX = -1
result = []

for i in range(1,n+1):
    c = bfs(i)
    if c > MAX:
        result = [i]
        MAX = c
    elif c == MAX:
        result.append(i)
        MAX = c

for e in result:
    print(e, end=" ")
