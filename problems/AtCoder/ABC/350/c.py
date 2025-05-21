# WA
N = int(input())
A = list(map(int, input().split()))

# 左端からi、右端からjの要素を見つけて正しい位置に置いていく
ans = []
i = 1
j = N
while i != j:
    for idx in range(i-1, j-1): # 未入替の範囲を見ていく
        if A[idx] == i:
            if A[idx] != idx+1:
                ans.append([A[idx], A[i-1]])
                A[idx], A[i-1] = A[i-1], A[idx]
            i += 1
            break
        elif A[idx] == j:
            if A[idx] != idx+1:
                ans.append([A[idx], A[j-1]])
                A[idx], A[j-1] = A[j-1], A[idx]
            j -= 1
            break

print(len(ans))
for a in ans:
    print(*a)