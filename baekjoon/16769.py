# Mixing Milk
C, M = [], []

for i in range(3):
    a, b = map(int, input().split())
    C.append(a)
    M.append(b)

for i in range(100):
    idx, nxt = i % 3, (i+1) % 3
    M[idx], M[nxt] = max(M[idx] - (C[nxt] - M[nxt]), 0), min(C[nxt], M[nxt] + M[idx])

for i in M:
    print(i)