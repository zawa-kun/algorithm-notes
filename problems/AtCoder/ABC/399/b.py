N = int(input())
P = list(map(int, input().split()))
sort_P = sorted(P, reverse=True)
r = 1
same_rank_cnt = 1

# 最下位-1 までの置き換え
for i in range(N - 1):
    # 同じ数が何個あるか数える.
    if sort_P[i] == sort_P[i+1]:
        same_rank_cnt += 1
        continue
    
    # 順位の置き換え.(同じ数字は全て同じ順位)
    for j in range(N):
        if P[j] == sort_P[i]:
            P[j] = r

    r += same_rank_cnt
    same_rank_cnt = 1

# 最下位の置き換え
for i in range(N):
    if P[i] == sort_P[-1]:
        P[i] = r

# 出力
for rank in P:
    print(rank)