# make N*N Grid
N = int(input())
G = [[0] * N for _ in range(N)]
print(G)

# 二次元配列の入力
N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
print(G)
