# 좌표 정렬하기
n = int(input())
arr = []
for _ in range(n):
    y, x = map(int, input().split(" "))
    arr.append((y, x))
arr = sorted(arr)
for i in arr:
    print(i[0], i[1])
