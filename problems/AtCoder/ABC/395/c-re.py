N = int(input())
A = list(map(int, input().split()))

idx = [list() for _ in range(10**6+1)]
ans = 1_000_001
for i, x in enumerate(A):
    idx[x].append(i)

for i in range(1_000_001):
    if len(idx[i]) < 2:
        continue

    for j in range(len(idx[i])-1):
        ans = min(ans, idx[i][j+1] - idx[i][j] + 1)

if ans == 1_000_001:
    print(-1)
else:
    print(ans)