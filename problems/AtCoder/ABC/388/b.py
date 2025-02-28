N, D = map(int, input().split()) # N:蛇の数 D:伸ばせる最大値.
T, L = [0]*N, [0]*N # 先にn個の配列を確保.
#太さと長さを受け取る.
for i in range(N):
    T[i], L[i] = map(int, input().split())

weights = []
# N匹目まで長さを1~D伸ばしたときの重量を計算.
for k in range(1, D+1):
    weights = []
    for i in range(N):  
        weight = T[i] * (L[i]+k) # 長さ＋Dをした状態の体重計算. 
        weights.append(weight)
    
    # 最大の値を出力.
    weights.sort()
    print(weights[-1])

    # maxを出力する時,↓でも可.
    # print(max(weights))

