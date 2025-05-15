import copy
S = str(input())
copy_S = list(S)
lower_idxs = []
supper_idxs = []

for i in range(len(S)):
    if S[i].islower():
        lower_idxs.append(i) # 小文字のインデックスを取得
    else:
        supper_idxs.append(i)

lower_cnt = len(lower_idxs)
supper_cnt = len(supper_idxs)

if lower_cnt < supper_cnt: 
    for idx in lower_idxs: # 大文字の方が多い場合小文字を変換
        copy_S[idx] = S[idx].upper()
else:
    for idx in supper_idxs:
        copy_S[idx] = S[idx].lower()

print("".join(copy_S))
