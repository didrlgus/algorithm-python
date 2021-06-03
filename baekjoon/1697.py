# 숨바꼭질
from collections import deque

n, k = map(int, input().split(" "))

MAX = 100001
visited = [0] * MAX

def bfs():
    visited[n]=0
    q = deque([n])
    while q:
        front = q.popleft()
        if front == k:
            return visited[front]
        for next in (front - 1, front + 1, front * 2):
            if 0 <= next < MAX and not visited[next]:
                visited[next]=visited[front]+1
                q.append(next)
        
print(bfs())