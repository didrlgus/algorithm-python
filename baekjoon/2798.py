# 블랙잭
n,m = list(map(int, input().split(' ')))
arr = list(map(int, input().split(' ')))
ret = 0
for i in range(1,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum=arr[i]+arr[j]+arr[k]
            if sum<=m:
                ret=max(ret,sum)

print(ret)