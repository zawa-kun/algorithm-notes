N, M = map(int, input().split())
G = [] # 食材表
for _ in range(M):
    row = list(map(int, input().split()))
    G.append(row[1:]) # 「1個目以降」を格納

B = list(map(int, input().split())) # i日目にi番目の材料を克服
result = 0 # 食べれる料理数
cnt = [0] * M # cnt[i] : 料理iに含まれる「まだ苦手な食材」
idx = [[] for _ in range(N)] # idx[x] : 食材iが含まれる料理のインデックスのリスト

for i, dish in enumerate(G): 
    cnt[i] = len(dish)
    for ingredient in dish:
        idx[ingredient-1].append(i)

for i in range(len(B)): # 1...N日目まで見ていく
    for v in idx[B[i]-1]: # 克服した野菜が入っている料理のリストを取り出す。
        cnt[v] -= 1 # 一つ克服したのでデクリメント
        if cnt[v] == 0: # カウント０つまり、苦手なものが一つも入っていないという事
            result += 1 # 食べれるものが一つ増える。
    print(result)
