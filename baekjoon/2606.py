# 바이러스
n = int(input())
k = int(input())

adj = [[] for _ in range(n+1)]

for _ in range(k):
    a, b = map(int, input().split(" "))
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (n+1)

ret = 0

def dfs(start):
    visited[start]=True
    
    for next in adj[start]:
        if not(visited[next]):
            global ret
            ret += 1
            dfs(next)

dfs(1)
print(ret)
