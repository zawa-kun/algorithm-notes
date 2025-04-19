Q = int(input())
querys = [list(map(int,input().split())) for _ in range(Q)]
que = []
for i in range(Q):
    if querys[i][0] == 1:
        que.append(querys[i][1])
    else:
        print(que.pop(0))
