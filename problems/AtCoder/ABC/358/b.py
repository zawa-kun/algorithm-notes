N, A = map(int, input().split())
T = list(map(int, input().split()))

now = 0
for i in range(N):
    if T[i] > now:
        now = T[i]
    now += A
    print(now)


    