N, C = map(int, input().split())
T = list(map(int, input().split()))

count = 1
before = T[0]
for i in range(1, N):
    if T[i] - before >= C:
        count += 1
        before = T[i]
print(count)

