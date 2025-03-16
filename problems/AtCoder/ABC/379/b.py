N, K = map(int, input().split())
S = list(input())

count = 0 # 連続している「O」の歯の数
eated_strawberry = 0 # 食べたイチゴの数

for i in range(N):
    if S[i] == "O":
        count += 1
        if count >= K:
            eated_strawberry += 1
            count = 0
    else: # "x"であるとき,リセットする.
        count = 0

print(eated_strawberry)

