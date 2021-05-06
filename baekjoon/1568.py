# 새
n = int(input())
k = 1
ret = 0
while n != 0:
    if n < k:
        k = 1
    n -= k
    k += 1
    ret += 1
print(ret)
