N = int(input())
P = list(map(int, input().split()))

P_sorted = sorted(P, reverse=True)
ans = [0]*N
r = 1
ans_set={}
ans_set[P_sorted[0]] = r
k = 0
for i in range(1, N):
    if P_sorted[i-1] != P_sorted[i]:
        r += 1+k
        k = 0
    else:
        k += 1
        
    ans_set[P_sorted[i]] = r

for p in P:
    print(ans_set[p])