N, K = map(int, input().split())
if N <= K:
    print(1)
    exit()

A = [0] * (N - K + 1) # K-1以前の配列は必要ない
sum = K
A[0] = 1
A[1] = K

for i in range(2, N - K + 1):
    # A[i] = A[i-1] + K + A[i-K]
    if i - K < 0:
        A[i] = sum + A[i - 1] - 1
        sum = A[i]
    else:
        A[i] = sum + A[i - 1] - A[i - K]
        sum = A[i]
print(A[-1])
print("----------------")
print(A[-1] % (10 ** 9))
print(A[N - K] % (10 ** 9))