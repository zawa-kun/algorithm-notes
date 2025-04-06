N, M = map(int, input().split())
AB = [input().split() for _ in range(M)]

flags = [False] * N # 家の個数のフラグ
for i in range(M):
    if AB[i][1] == 'M' and flags[int(AB[i][0]) - 1] == False:
        flags[int(AB[i][0]) - 1] = True 
        print('Yes')
    else:
        print('No')