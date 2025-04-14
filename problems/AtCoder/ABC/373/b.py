S = str(input())
alpha_map = [0] * 26

distance = 0
# 各文字の位置を格納
for i in range(len(S)):
    alpha_map[ord(S[i]) - ord('A')] = i 

# 距離計算
for i in range(1, len(alpha_map)):
    distance += abs(alpha_map[i] - alpha_map[i-1])
print(distance)