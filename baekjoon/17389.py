# 보너스 점수
N, S = input(), input()

score, bonus = 0, 0

for idx, OX in enumerate(S):
    if OX == 'O':
        score, bonus = score+idx+1+bonus, bonus+1
    else:
        bonus=0

print(score)

# N = int(input())
# OX = input()

# bonus = 0
# ret = 0

# for i in range(1, N+1):
#     if OX[i-1] == 'O':
#         ret+=i+bonus 
#         bonus+=1    
#     else:
#         bonus=0

# print(ret)