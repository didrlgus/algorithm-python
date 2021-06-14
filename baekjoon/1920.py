# 수 찾기
N, A = int(input()), {i : 1 for i in list(map(int, input().split()))}
M = int(input())
for i in list(map(int, input().split())):
    print(A.get(i, 0))

# n = int(input())
# arr = set(map(int, input().split()))
# m = int(input())
# x = list(map(int, input().split()))

# for i in x:
#     if i not in arr:
#         print('0')
#     else:
#         print('1')