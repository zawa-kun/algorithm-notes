H, W, D = map(int, input().split())
S = [input() for _ in range(H)]

ans = 0
for i1 in range(H):
    for j1 in range(W):
        if(S[i1][j1] == '#'):
            continue # 床のマスではない
        for i2 in range(H):
            for j2 in range(W):
                if S[i2][j2] == '#' or i1 == i2 and j1 == j2:
                    continue # 床のマスではないか片方の加湿器と同じ場所
                tmp = 0
                for i in range(H):
                    for j in range(W):
                        if S[i][j] == '.':
                            if abs(i-i1) + abs(j-j1) <= D or abs(i-i2) + abs(j-j2) <= D:
                                tmp += 1 # 「床」　かつ　「マンハッタン距離がD以内」のとき
                ans = max(ans, tmp)
        
print(ans)
