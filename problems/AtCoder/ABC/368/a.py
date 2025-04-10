N, K = map(int, input().split())
A = input().split()
A = A[-(K):] + A[:-(K)]
print(*A)