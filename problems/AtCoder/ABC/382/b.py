N, D = map(int, input().split())
S = input()
S_list = []
#Sをリストに変換.
for i in range(N):
    S_list.append(S[i])

# D日経った時の最後に食べたcookieより右側の箱の中身
result = []
while D > 0:
    if S_list[-1] == ".":
        result.append(S_list.pop())
    else:
        result.append(".")
        S_list.pop()
        D -= 1 # cookieはD日間の間食べるため、cookieを食べたらDを減らす.

# 最後のcookieより左側を出力.
for i in range(N - len(result)):
    print(S_list[i], end="")
    
# 最後のcookieより右側を出力.
for i in range(len(result)):
    print(result[i], end="")
