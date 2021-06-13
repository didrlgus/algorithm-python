# 거스름돈
n = 1000-int(input())

ret = 0

for coin in [500, 100, 50, 10 , 5, 1]:
    ret += n // coin
    n %= coin

print(ret)