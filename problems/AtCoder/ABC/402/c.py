N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(M)] # 食材表
B = list(map(int, input().split())) # i日目にi番目の材料を克服

ingredients = [set()]*M # 材料の分布
for i in range(M):
    ingredients[i] = set(G[i])

for i in range(len(B)):
    # 苦手克服した食べ物を削除
    cnt = 0
    for j in range(len(ingredients)):
        ingredients[j].discard(B[i])
        if len(ingredients[j]) == 0:
            cnt += 1

    print(cnt)