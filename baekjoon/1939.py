# 중량제한
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

start = 1000000000
end = 1


def bfs(cost):
    queue = [start_node]
    visited = [False] * (n + 1)
    visited[start_node] = True
    while queue:
        x = queue.pop(0)
        for y, weight in adj[x]:
            if not visited[y] and weight >= cost:
                visited[y] = True
                queue.append(y)
    return visited[end_node]


for _ in range(m):
    x, y, weight = map(int, input().split())
    adj[x].append((y, weight))
    adj[y].append((x, weight))
    start = min(start, weight)
    end = max(end, weight)

start_node, end_node = map(int, input().split())

result = start
while start <= end:
    mid = (start + end) // 2
    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)
