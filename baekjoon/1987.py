# 알파벳
r, c = map(int, input().split())
arr = []
ret = 0

def bfs(y, x):
    global ret
    q = set()
    q.add((y, x, arr[y][x]))

    while q:
        y,x,step = q.pop()
        ret = max(ret, len(step))

        for dir in ((0,1),(0,-1),(1,0),(-1,0)):
            ny = y + dir[0]
            nx = x + dir[1]

            if (ny<0 or nx<0 or ny>=r or nx>=c):
                continue
            if arr[ny][nx] not in step:
                q.add((ny,nx,step+arr[ny][nx]))

for _ in range(r):
    arr.append(input())

bfs(0, 0)
print(ret)