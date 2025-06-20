N, M = map(int, input().split())
B = list(map(int, input().split()))
W = list(map(int, input().split()))

B.sort(reverse=True) # 降順並び替え
W.sort(reverse=True) # 降順並び替え

G = [0] * N
total = 0
Wi = 0
for Bi in range(N): # 黒を取り出していく.
    # 白を黒以下の個数で取り出していく.
    total += B[Bi] # Bi個選んだ時のBの最大
    # 白ボールのインデックスWiがリスト内で、かつ価値が正ならば加算する
    # （負の価値の白ボールは選ばない方が得なので）
    if Wi <= M-1 and 0 < W[Wi]: 
        total += W[Wi]
    G[Bi] = total
    Wi += 1

result = max(G)
if max(G) < 0:
    result = 0
print(result)