# 프린터 큐
tc = int(input())
for _ in range(tc):
    cnt = 0
    n, m = list(map(int, input().split(" ")))
    queue = list(map(int, input().split(" ")))
    queue = [(i, idx) for idx, i in enumerate(queue)]
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            cnt += 1
            if queue[0][1] == m:
                print(cnt)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))