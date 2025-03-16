S = list(input())

count = 0 # ボタンを押す回数.
flag = False # 0が連続しているかどうかを管理するフラグ.

for i in range(len(S)):
    if S[i] == "0":
        if flag:
            flag = False
        else:
            flag = True
            count += 1
    else:
        count += 1
        flag = False

print(count)