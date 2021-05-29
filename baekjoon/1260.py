# DFS와 BFS
def dfs(start):
    visited[start] = True
    print(start, end=" ")
    for v in adj[start]:
        if not(visited[v]):
            dfs(v)

def bfs(start):
    visited[start] = True
    queue = list()
    queue.append(start)

    while queue:
        prev = queue.pop(0)
        print(prev, end=" ")
        for next in adj[prev]:
            if not(visited[next]):
                visited[next] = True
                queue.append(next)

n,m,v = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for e in adj:
    e.sort()

visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)