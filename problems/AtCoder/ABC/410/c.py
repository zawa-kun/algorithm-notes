N, Q = map(int, input().split())
Querys = [list(map(int, input().split())) for _ in range(Q)]

A_idxs = [int(x) + 1 for x in range(N)] # listのスライスを使えばシフト速そう

for query in Querys:
    if query[0] == 1:
        A_idxs[query[1]-1] = query[2]
    elif query[0] == 2:
        print(A_idxs[query[1]-1])
    elif query[0] == 3:
        k = query[1]
        slide_length = k % N
        A_idxs = A_idxs[slide_length:] + A_idxs[:slide_length]