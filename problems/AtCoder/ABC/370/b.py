N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
# print(A)

x = 0
for y in range(N):
    if x-1  >= y:
        x = A[x-1][y]
    else:
        x = A[y][x-1]

print(x)