# 센서
import sys

n = int(input())
k = int(input())

if k >= n:
    print(0)
    sys.exit()

arr = list(map(int, input().split()))
arr.sort()

diff = []

for i in range(0, len(arr) - 1):
    diff.append(arr[i+1] - arr[i])

diff.sort(reverse=True)

for i in range(0, k-1):
    diff[i]=0

print(sum(diff))