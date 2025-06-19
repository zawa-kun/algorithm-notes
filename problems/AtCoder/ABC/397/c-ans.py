N = int(input())
A = list(map(int, input().split()))

lcnt = [0]*N
value_set = set()
for i in range(N):
    value_set.add(A[i])
    lcnt[i] = len(value_set)

rcnt = [0]*N
value_set = set()
for i in range(N-1, -1, -1):
    value_set.add(A[i])
    rcnt[i] = len(value_set)

max = 0
for i in range(N-1):
    total = lcnt[i]+rcnt[i+1]
    if max < total:
        max = total
print(max)