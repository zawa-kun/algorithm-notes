# 解けなかった為、模範解答.
N, M = map(int, input().split()) # N: Sの行数、列数, M: Tの行数、列数.
# N, M = 3, 2
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

# a,bを基準に見ていく.
for a in range(N - M + 1):
    for b in range(N - M + 1):
        ok = True
        for i in range(M):
            for j in range(M):
                # Sのa+i行目のb+j列目とTのi行目j列目が一致しない場合はokをFalseにする.
                if S[a+i][b+j] != T[i][j]:
                    ok = False
        #　同じモノが存在した場合,
        if ok == True:
            print(a+1, b+1)
