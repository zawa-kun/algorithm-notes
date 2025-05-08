N, L, R = map(int, input().split())
A = [int(x) for x in range(1, N+1)]
rev_A = A[L-1:R]
rev_A.reverse()

print(*(A[:L-1] + rev_A + A[R:]))
