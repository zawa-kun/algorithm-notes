imos = [0] * 11  # サイズ+1（右端対策）

# 操作を加える
imos[2] += 1
imos[5] -= 1

# 累積和をとる
for i in range(1, 11):
    imos[i] += imos[i - 1]

# 最終的な配列（imos[0]〜imos[9]）が答え
print(*imos)