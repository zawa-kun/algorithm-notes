N, M = map(int, input().split())

wall = [0] * (N+1)
for _ in range(M):
    L, R = map(int, input().split())
    wall[L-1] += 1
    wall[R] -= 1


for i in range(1, N):
    wall[i] += wall[i-1]

print(min(wall[:N]))