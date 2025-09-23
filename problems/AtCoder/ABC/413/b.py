N = int(input())

S = [input() for i in range(N)]

# 連結した文字列の重複を取り除くためにsetを使う
ans = set()
for s in S:
    for t in S:
        if s != t: # 異なる二つの文字列を
            ans.add(s + t) # 連結して追加

print(len(ans))