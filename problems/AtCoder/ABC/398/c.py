N = int(input())
A = list(map(int, input().split()))

d = {}
for i in range(N):
    d.setdefault(A[i], 0)
    d[A[i]] += 1

max_value = 0
ans = None
for k, v in d.items():
    if v == 1 and k >= max_value:
            max_value = k


if max_value != 0:
    ans = A.index(max_value) + 1
    print(ans)
else:
    print(-1)