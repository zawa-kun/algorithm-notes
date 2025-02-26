#長さを昇順に並び替えて、出力
N = int(input()) # 受け取る文字列の数.
S = list(input() for _ in range(N)) # 受け取った文字列のリスト.

#最大数が50のため、バブルソートでも可能.
#バブルソートを用いて文字列の長さを昇順に並び替える.
for i in range(N):
    for j in range(N - 1 - i):
        len_j = len(S[j]) #文字列の長さ
        len_incj = len(S[j+1]) #文字列の長さ.
        if len_j > len_incj:
            S[j], S[j+1] = S[j+1], S[j]

#昇順に並び替えた文字列を結合して出力.
for i in range(N):
    print(S[i], end="")