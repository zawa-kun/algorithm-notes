S, T = input().split()

for w in range(1, len(S)):
    for c in range(w):
        now = ""
        for i in range(c, len(S), w): # w文字ずつ区切った各ブロックのc文字目の連結
            now += S[i]
        if now == T:
            print("Yes")
            exit()

print("No")