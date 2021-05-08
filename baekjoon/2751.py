# 수 정렬하기 2
n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array = sorted(array)

for data in array:
    print(data)
