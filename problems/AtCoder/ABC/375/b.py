def calculate_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

if __name__ == "__main__":
    N = int(input())
    G = [list(map(int, input().split())) for _ in range(N)]

    total_distance = 0
    for i in range(N):
        # 原点から最初の座標の移動距離を加算
        if i == 0:
            total_distance += calculate_distance(0, 0, G[i][0], G[i][1])
            continue
        # 前の座標からの移動距離を加算
        total_distance += calculate_distance(G[i-1][0], G[i-1][1],G[i][0], G[i][1])
    # 最後の座標から原点の移動距離を加算
    total_distance += calculate_distance(G[i][0], G[i][1], 0, 0)
    
    print(total_distance)