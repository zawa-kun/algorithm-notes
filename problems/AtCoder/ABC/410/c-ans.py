N, Q = map(int, input().split())
Querys = [list(map(int, input().split())) for _ in range(Q)]

A = [int(x) for x in range(1, N+1)]
offset = 0 # ずれ
for q in Querys:
    if q[0] == 1: # 置き換え
        A[(q[1]-1+offset) % N] = q[2]
    elif q[0] == 2: # 出力
        print(A[(q[1]-1+offset) % N]) # indexに合わせるために-1
    elif q[0] == 3:
        offset += q[1] % N
        offset %= N
        
