N = int(input())
qr = [list(map(int, input().split())) for _ in range(N)] # ゴミの分別表
Q = int(input())
td = [list(map(int, input().split())) for _ in range(Q)] # d日にtのゴミが出る

for i in range(Q):
    trash = td[i][0] - 1 # ゴミの種類
    day = td[i][1] # この日以降
    q, r = qr[trash]

    # 切り上げ除算をする
    k = max((day - r + q - 1) // q, 0)
    print(q * k + r)