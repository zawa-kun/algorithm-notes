N = int(input())
A = list(map(int, input().split()))
pos = [0] * (N+1) # 各値がどこにあるかを記録
ans = []

for idx, val in enumerate(A):
    pos[val] = idx

for i in range(N):
     # i番目にあるべき値は(i+1)である
    if A[i] != i + 1:
        # i番目にあるべき値が今どこにあるかを確認する
        """
        ここで
        posがあることで目的の値がどこにあるかをO(1)で見つけ出せる
        """
        correct_val = i + 1
        j = pos[correct_val]

        # 交換する
        A[i], A[j] = A[j], A[i]
        # posを更新
        pos[A[j]] = j
        pos[A[i]] = i

        # 操作を記録
        ans.append((i + 1, j + 1))
    
print(len(ans))
for i, j in ans:
    print(i, j)
