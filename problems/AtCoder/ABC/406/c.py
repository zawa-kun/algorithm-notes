N = int(input())
P = list(map(int, input().split()))

# P から大小関係の文字列 S を作る
S = ""
for i in range(N-1):
    if P[i] < P[i+1]:
        S += "<"
    else:
        S += ">"

# ランレングス圧縮（RLE）
RLE_S = []
cnt = 1
for i in range(1, len(S)):
    if S[i] == S[i-1]:
        cnt += 1
    else:
        RLE_S.append((S[i-1], cnt))
        cnt = 1
RLE_S.append((S[-1], cnt))

# チルダ型の数え上げ
ans = 0
for i in range(1, len(RLE_S) - 1):
    if RLE_S[i-1][0] == '<' and RLE_S[i][0] == '>' and RLE_S[i+1][0] == '<':
        ans += RLE_S[i-1][1] * RLE_S[i+1][1]

print(ans)

