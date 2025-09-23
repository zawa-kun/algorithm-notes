N, M = map(int, input().split())
A = list(map(int, input().split()))

total_weight = 0
for i in range(N):
    total_weight += A[i]
    if total_weight > M:
        print("No")
        exit()

print("Yes")