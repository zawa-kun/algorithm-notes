N, T = map(int,input().split())
A = list(int(x) - 1 for x in input().split()) 

row = [0] * N
col = [0] * N
diag = [0] * 2
for i in range(T):
    # マスの番号Aiを座標(i,j)に変換
    x = A[i] // N
    y = A[i] % N
    # 横
    row[x] += 1
    if row[x] == N:
        print(i + 1)
        exit()
    # 縦
    col[y] += 1
    if col[y] == N:
        print(i + 1)
        exit()
    # 左上 - 右下 方向の斜め
    if x == y:
        diag[0] += 1
        if diag[0] == N:
            print(i + 1)
            exit()
    # 右上 - 左下 方向の斜め
    if x + y == N - 1:
        diag[1] += 1
        if diag[1] == N:
            print(i + 1)
            exit()
print(-1)