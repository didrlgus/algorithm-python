# 공유기 설치
n, c = list(map(int, input().split(" ")))

array = []

for _ in range(n):
    array.append(int(input()))

array = sorted(array)

start = 1
end = array[-1] - array[0]
ret = 0

while start <= end:
    mid = (start + end) // 2
    val = array[0]
    cnt = 1
    for i in range(1, len(array)):
        if array[i] >= val + mid:
            val = array[i]
            cnt += 1
    if cnt >= c:
        start = mid + 1
        ret = mid
    else:
        end = mid - 1
print(ret)
