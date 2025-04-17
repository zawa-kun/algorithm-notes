N = int(input())
P = list(map(int, input().split()))

sort_P = sorted(P, reverse=True)
r = 1
same_rank_cnt = 1

for i in range(N - 1):
    idx = P.index(sort_P[i])
    P[idx] = r
    if sort_P[i] == sort_P[i+1]:
        same_rank_cnt += 1
        continue

    r += same_rank_cnt
    same_rank_cnt = 1

P[P.index(sort_P[-1])] = r

# output
for rank in P:
    print(rank)