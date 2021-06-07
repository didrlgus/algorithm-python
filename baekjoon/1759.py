# 암호 만들기
from itertools import combinations

vowels = ('a','e','i','o','u')
l,c = map(int,input().split())

arr = input().split()
arr.sort()

for password in combinations(arr, l):
    cnt = 0
    for i in password:
        if i in vowels:
            cnt += 1
    if cnt>=1 and l-cnt>=2:
        print(''.join(password))

# l,c = map(int,input().split())

# arr = list(input().split())

# arr.sort()

# vowel = "aeiou"

# def dfs(a, b, idx, ret):
#     if len(ret) == l:
#         if a>=1 and b>=2:
#             print(ret)
#         return
#     for i in range(idx, c):
#         if arr[i] in vowel:
#             dfs(a+1,b,i+1,ret+arr[i])
#         else:
#             dfs(a,b+1,i+1,ret+arr[i])

# dfs(0,0,0,"")
