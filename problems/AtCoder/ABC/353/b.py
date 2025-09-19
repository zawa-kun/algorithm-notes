from collections import deque

N, K = map(int, input().split())

A = deque(map(int, input().split()))

cnt = 0
while len(A) != 0:
    K_now = K
    while len(A) != 0 and K_now >= A[0]:
        K_now -= A.popleft()
    cnt += 1

print(cnt)