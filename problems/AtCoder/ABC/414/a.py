N, L, R = map(int, input().split())
cnt = 0
for _ in range(N):
    X, Y = map(int, input().split())
    if X <= L and R <= Y:
        cnt += 1

print(cnt)