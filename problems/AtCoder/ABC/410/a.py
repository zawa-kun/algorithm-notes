N = int(input())
A = list(map(int, input().split()))
K = int(input())
cnt = 0
for Ai in A:
    if Ai >= K:
        cnt += 1

print(cnt)