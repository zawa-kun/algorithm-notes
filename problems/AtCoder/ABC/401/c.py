N, K = map(int, input().split())

A = [1] * (N + 1)
s = K

for i in range(K, N+1):
    A[i] = s
    s -= A[i - K]
    s += A[i]
    # MODを取ることで, 0 ~ MOD-1 の間に収める
    # 大きすぎると計算に時間がかかり、TLE
    s %= 10**9 

print(A[N] % (10 ** 9))