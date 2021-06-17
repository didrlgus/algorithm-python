# 수빈이와 수열
n, arr = int(input()), list(map(int, input().split()))

ret = [arr[0]]
sum = arr[0]
    
for i in range(1, len(arr)):
    y = arr[i]*(i+1)-sum
    ret.append(y)
    sum+=y

for el in ret:
    print(el, end=" ")