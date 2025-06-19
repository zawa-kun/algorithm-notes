N = int(input())
A = list(map(int, input().split()))

all = len(set(A))*2
idx = [0]*(N+1) # idx[x]: 値ｘの数
for x in A:
    idx[x] += 1

max = 0
k = len(set(A))
for i in range(N):
    idx[A[i]] -= 1
    if idx[A[i]] == 0:
        k -= 1 # 片方にすべて入り切ったという事だから。
    else: 
        k += 1
    total = all - k
    
    if max < total:
        max = total
print(max)
    
    