# 유기농 배추
import sys
sys.setrecursionlimit(100000)

def dfs(y, x):
    visited[y][x] = True
    for dy,dx in [(0,1),(0,-1),(1,0),(-1,0)]:
        ny, nx = y + dy, x + dx
        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue
        if visited[ny][nx]:
            continue
        if arr[ny][nx]:
            dfs(ny, nx)

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    
    visited = [[False] * m for _ in range(n)]

    ret = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j]==1 and not(visited[i][j]):
                dfs(i, j)
                ret += 1
    print(ret)