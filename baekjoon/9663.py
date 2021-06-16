# N-Queen
n = int(input())
row = [0] * (n+1)
ret = 0
i = 0

def check(x):
    for i in range(x):
        if row[x] == row[i]:
            return False
        if abs(row[x] - row[i]) == x - i:
            return False
    return True

def dfs(r):
    if r == n:
        global ret
        ret += 1
        return

    for j in range(n):
        row[r] = j
        if check(r):
            dfs(r+1)

dfs(0)
print(ret)