N = 3
items = ['A', 'B', 'C']

# 2^N通りの部分集合をループ
for i in range(1 << N): # 2^Nと同義.
    selected_subset = []
    for j in range(N):
        if (i >> j) & 1: # i のj番目が1であればTrue
            selected_subset.append(items[j])
    print(f"整数{i} (二進数: {bin(i)}: 選択された部分集合: {selected_subset}")
