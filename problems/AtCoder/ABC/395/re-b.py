N = int(input())
G = list([None]*N for _ in range(N))

for i in range(N):
    j = N - 1 - i # 1度のループで塗る1辺の長さ.
    if  i <= j:
        for x in range(i, j + 1):
            for y in range(i, j + 1):
                if i % 2 == 0:    # iが偶数のとき
                    G[x][y] = "#"
                else:             # iが奇数のとき
                    G[x][y] = "."

# 出力
for x in range(len(G)):
    for y in range(len(G)):
        print(G[x][y],end="")
    print()
        
                
            
        