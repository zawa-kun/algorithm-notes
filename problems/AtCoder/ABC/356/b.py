N, M = map(int, input().split())
A = list(map(int, input().split())) # 必要な栄養素の量
X = [list(map(int, input().split())) for _ in range(N)]
intake_amounts = [0]*M # 実際の栄養素ごとの摂取量

for i in range(N):
    for j in range(M):
        intake_amounts[j] += X[i][j]

flag = True
for i in range(M):
    if intake_amounts[i] < A[i]:
        flag = False

if flag:
    print("Yes")
else:
    print("No")