a = list(map(int, input().split(' ')))

ascending = True
descending = True

for i in range(1,8):
    if a[i-1] < a[i]:
        descending = False
    else:
        ascending = False

if ascending == True:
    print('ascending')
elif descending == True:
    print('descending')
else:
    print('mixed')