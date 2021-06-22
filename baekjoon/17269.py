# 이름궁합 테스트
N, M = map(int, input().split())
A, B = input().split()

alpha = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]

AB = ''
mn = min(N,M)
for i in range(mn):
    AB += A[i] + B[i]

AB += A[mn:] + B[mn:]

arr = [alpha[ord(i) - ord('A')] for i in AB]

for i in range(N+M-2):
    for j in range(N+M-1-i):
        arr[j] += arr[j+1]

print("{}%".format(arr[0]%10*10 + arr[1]%10))
