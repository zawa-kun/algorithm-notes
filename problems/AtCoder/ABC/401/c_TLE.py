N, K = map(int, input().split())

A = [1] * (N + 1)
sum = K

for i in range(K, N+1):
    A[i] = sum + A[i - 1] - A[i - (K+1)]
    sum = A[i]
# print("----------------")
print(A[N] % (10 ** 9))