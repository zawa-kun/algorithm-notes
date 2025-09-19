from collections import deque

N, K = map(int, input().split())

A = deque(map(int, input().split()))

cnt = 0
while len(A) != 0:
    K_now = K # ride_countsやseats_leftとかの方が読みやすい
    while len(A) != 0 and K_now >= A[0]:
        K_now -= A.popleft() # dequeで無理やりpopleftしなくてもインデックスで順次処理でも今回の制約では十分。
    cnt += 1

print(cnt)